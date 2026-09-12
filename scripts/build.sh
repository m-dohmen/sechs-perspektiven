#!/usr/bin/env bash
# Baut dist/sechs-perspektiven.zip (Upload in Cowork/claude.ai, Entpacken für
# Codex und Claude Code) sowie die identische Kopie
# dist/sechs-perspektiven.skill als Release-Artefakt.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAME="sechs-perspektiven"
SRC="$ROOT/skills/$NAME"
STAGE="$(mktemp -d)"
OUT="$ROOT/dist/$NAME.zip"
SKILL="$ROOT/dist/$NAME.skill"

mkdir -p "$STAGE/$NAME/references"
cp "$SRC/SKILL.md" "$STAGE/$NAME/"
cp "$SRC/references/beispielsitzung.md" "$STAGE/$NAME/references/"
cp "$SRC/references/dach-pruefpunkte.md" "$STAGE/$NAME/references/"
cp "$SRC/references/moderation.md" "$STAGE/$NAME/references/"

mkdir -p "$ROOT/dist"
rm -f "$OUT" "$SKILL"
(cd "$STAGE" && zip -qr "$OUT" "$NAME")
cp "$OUT" "$SKILL"
rm -rf "$STAGE"

echo "gebaut: $OUT"
echo "gebaut: $SKILL"
