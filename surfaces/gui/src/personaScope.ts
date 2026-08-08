// A persona is "project-scoped" only when it's code-family: an explicit directory the user
// picks, sessions grouped by project in the sidebar. Everything else (knowledge, chat) runs on
// a transparent per-conversation scratch dir, with real folders added as roots when needed —
// no folder gate, ever. (The old workspace enum — git/project/deliverable/none — collapsed
// into family; owner decision 2026-07-03, UX-DECISIONS §16.)
export function isProjectScoped(p?: { workspace?: string; family?: string }): boolean {
  return p?.family === "code";
}

// Persona naming: the product-facing assistant is PAVii. Internal ids keep their legacy names for
// compatibility, but chrome and search never expose "coworker" as a product label.

// Short label for the sidebar + top bar: "PAVii" / "Code" / "Ops" / "Chat".
export function shortPersonaName(name?: string, id?: string): string {
  if (id === "cowork") return "PAVii";
  const n = (name || id || "").trim();
  return n.replace(/\s*coworker$/i, "").trim() || n;
}

// Full display name for the persona detail page. Chat isn't a PAVii persona — left as-is.
export function fullPersonaName(name?: string, id?: string): string {
  if (id === "cowork") return "PAVii";
  const n = (name || id || "").trim();
  if (id === "chat" || !n) return n;
  return n.replace(/\s*coworker$/i, "").trim() || n;
}
