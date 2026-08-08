"""Sidecar loopback routes for PAVii connector relay and gallery removal.

PAVii keeps local connector OAuth callbacks, signed-out local operation, and a
PAVii-branded connector relay surface. Hosted relay sign-in stays disabled for
Phase 1 until PAVii-owned external provider apps are ready. The old product
gallery routes must remain unreachable.
"""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from coworker.server import SessionManager, create_app


def _allow_managed_state(state: str = "s") -> None:
    from coworker import cloud

    cloud._pending_managed_states[state] = cloud._now()


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("COWORKER_STATE_DIR", str(tmp_path / "state"))
    manager = SessionManager(workspace=tmp_path)
    app = create_app(manager)
    with TestClient(app) as c:
        c.manager = manager
        yield c


def test_connector_relay_sign_in_routes_are_parked_and_gallery_removed(client, monkeypatch):
    opened: list[str] = []
    monkeypatch.setattr("webbrowser.open", lambda url: opened.append(url))

    status = client.get("/v1/cloud/status")
    assert status.status_code == 200
    assert status.json()["signed_in"] is False

    telemetry = client.post("/v1/cloud/telemetry", json={"enabled": False})
    assert telemetry.status_code == 200
    assert telemetry.json()["telemetry_enabled"] is False

    login = client.post("/v1/cloud/login")
    assert login.status_code == 200
    assert login.json()["ok"] is False
    assert "coming soon" in login.json()["error"].lower()
    assert opened == []

    callback = client.get("/v1/auth/callback", params={"error": "access_denied"})
    assert callback.status_code == 400
    assert "PAVii connector relay sign-in" in callback.text

    assert client.get("/v1/cloud/gallery").status_code == 404
    assert client.get("/auth/callback", params={"code": "c", "state": "s"}).status_code == 404


def test_connect_managed_requires_sign_in(client):
    body = client.post("/v1/connectors/notion/connect-managed").json()
    assert not body["ok"]
    assert "coming soon" in body["error"].lower()


def test_oauth_callback_writes_profile_and_returns_page(client):
    _allow_managed_state()
    resp = client.post(
        "/oauth/callback",
        data={
            "provider": "google",
            "connector": "gmail",
            "connection_id": "conn_9",
            "access_token": "ya29.tok",
            "refresh_token": "1//r",
            "expires_in": "3599",
            "scope": "gmail.readonly",
            "account": "a@b.c",
            "app_state": "s",
        },
    )
    assert resp.status_code == 200
    # §30: the loopback page is a branded card, Title-cased connector name.
    assert "Gmail connected" in resp.text
    assert "Served locally by PAVii" in resp.text

    # Multi-account: the callback lands in gmail:account:<email>; gmail:default
    # is just the default pointer.
    profile = client.manager.secrets.get("gmail:account:a@b.c")
    assert profile["access_token"] == "ya29.tok"
    assert profile["managed"] is True
    assert profile["connection_id"] == "conn_9"
    assert client.manager.secrets.get("gmail:default")["default_account"] == "a@b.c"

    listed = {c["name"]: c for c in client.manager.list_connectors()}
    assert listed["gmail"]["connected"]
    assert listed["gmail"]["account"] == "a@b.c"
    assert [a["email"] for a in listed["gmail"]["accounts"]] == ["a@b.c"]


def test_oauth_callback_error_shows_failure_page(client):
    _allow_managed_state()
    resp = client.post(
        "/oauth/callback",
        data={"connector": "gmail", "error": "access_denied", "app_state": "s"},
    )
    assert resp.status_code == 400
    assert "access_denied" in resp.text
    assert client.manager.secrets.get("gmail:default") is None


def test_oauth_callback_rejects_unmanaged_connector(client):
    # telegram is manual-only (github gained a managed path with the App relay)
    _allow_managed_state()
    resp = client.post(
        "/oauth/callback",
        data={"connector": "telegram", "access_token": "x", "app_state": "s"},
    )
    assert resp.status_code == 400
    assert client.manager.secrets.get("telegram:default") is None


def test_oauth_callback_rejects_unknown_and_replayed_state(client):
    form = {
        "provider": "google",
        "connector": "gmail",
        "access_token": "token",
        "account": "a@b.c",
        "app_state": "once",
    }
    assert client.post("/oauth/callback", data=form).status_code == 400
    assert client.manager.secrets.get("gmail:default") is None

    _allow_managed_state("once")
    assert client.post("/oauth/callback", data=form).status_code == 200
    assert client.post("/oauth/callback", data=form).status_code == 400


def test_disconnect_works_signed_out(client):
    # manual profile, no cloud session: disconnect must not require the cloud
    client.manager.secrets.put("gmail:default", {"type": "oauth", "access_token": "t"})
    body = client.post("/v1/connectors/gmail/disconnect").json()
    assert body["ok"]
    assert client.manager.secrets.get("gmail:default") is None


SALES_MANIFEST = """---
id: sales
name: Sales Coworker
icon: chart
tagline: t
family: knowledge
workspace: deliverable
tools: [files, search, todo]
description: d
---
You are the Sales Coworker."""


def test_gallery_slug_persona_install_is_removed(client):
    body = client.post("/v1/personas/install", json={"gallery_slug": "sales"}).json()
    assert not body["ok"]
    assert "dir" in body["error"] and "git_url" in body["error"]


def test_delete_persona_refuses_builtin_and_unknown(client):
    body = client.delete("/v1/personas/cowork").json()
    assert not body["ok"] and "built-in" in body["error"]
    body = client.delete("/v1/personas/ghost").json()
    assert not body["ok"] and "unknown" in body["error"]
