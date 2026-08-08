import { platformOS } from "./tauri";

type ShortcutEvent = Pick<KeyboardEvent, "key" | "metaKey" | "ctrlKey" | "altKey" | "shiftKey">;

export function isMacOS(): boolean {
  return platformOS() === "macos";
}

export function isPrimaryShortcut(e: ShortcutEvent): boolean {
  return isMacOS() ? e.metaKey : e.ctrlKey;
}

export function resultShortcutLabel(index: number): string {
  return isMacOS() ? `⌘${index}` : `Ctrl+${index}`;
}

export function sidebarShortcutLabel(): string {
  return isMacOS() ? "⌘B" : "Ctrl+B";
}

export function settingsShortcutLabel(): string {
  return isMacOS() ? "⌘," : "Ctrl+S";
}

export function isSidebarShortcut(e: ShortcutEvent): boolean {
  return isPrimaryShortcut(e) && !e.altKey && !e.shiftKey && e.key.toLowerCase() === "b";
}

export function isSettingsShortcut(e: ShortcutEvent): boolean {
  const key = e.key.toLowerCase();
  if (isMacOS()) return e.metaKey && !e.ctrlKey && !e.altKey && key === ",";
  return e.ctrlKey && !e.metaKey && !e.altKey && key === "s";
}
