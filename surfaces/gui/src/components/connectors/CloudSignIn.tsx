// Phase 1 ships manual/local connectors only. Keep the connector-relay affordance
// visible so users know what is planned, but do not start hosted OAuth until the
// PAVii-owned provider apps and relay are ready.

// The signed-out state of every one-click pane: a REAL sign-in button, not a
// hint pointing at another page. Sign-in completes in the system browser; this
// component then polls until the status flips and broadcasts CLOUD_CHANGED, so
// even poll-less hosts (the Sources rail's inline pane) re-render signed in —
// relying on "some other section's 5s poll" left the rail stuck on the prompt
// (FB-013).
export function CloudSignInInline({ blurb }: { blurb?: string }) {
  return (
    <div className="space-y-1.5">
      <button
        className="w-full px-3 py-2 rounded-lg border border-line text-muted text-[13px] font-medium bg-paper opacity-70 cursor-not-allowed"
        data-testid="inline-cloud-sign-in"
        disabled
      >
        PAVii connector relay · Coming soon
      </button>
      <div className="text-[11.5px] text-faint">
        {blurb || "One-click PAVii connector relay is coming soon. Use Manual setup for now."}
      </div>
    </div>
  );
}

// The UNKNOWN state: the status fetch hasn't resolved (or is being retried).
// Rendering the sign-in prompt here told signed-in users they weren't (FB-013) —
// pending must look like pending.
export function CloudStatusPending() {
  return (
    <div
      className="text-[12px] text-faint py-2 text-center"
      data-testid="cloud-status-pending"
    >
      PAVii connector relay is coming soon.
    </div>
  );
}
