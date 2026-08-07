"""Sidecar loopback routes after Phase 1 account/gallery removal.

PAVii keeps local connector OAuth callbacks and signed-out local operation, but
the old product account and cloud gallery routes must remain unreachable.
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


def test_product_account_cloud_routes_are_removed(client):
    assert client.get("/v1/cloud/status").status_code == 404
    assert client.post("/v1/cloud/telemetry", json={"enabled": False}).status_code == 404
    assert client.get("/v1/cloud/gallery").status_code == 404
    assert client.get("/auth/callback", params={"code": "c", "state": "s"}).status_code == 404


def test_connect_managed_requires_sign_in(client):
    # notion, not gmail: the Google trio is managed_paused (CASA pending) and its
    # guard fires before the sign-in check — see test_google_one_click_paused….
    body = client.post("/v1/connectors/notion/connect-managed").json()
    assert not body["ok"]
    assert "not signed in" in body["error"]


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
