#!/usr/bin/env bash
# Rendert die PNG-Dateien in assets/: das Icon aus assets/icon.svg, das Social
# Preview aus den Zeichenanweisungen in scripts/social.py. Braucht ImageMagick
# und Python 3, keinen Browser. Nur zum Neubauen – die fertigen PNGs liegen im
# Repository.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ASSETS="$ROOT/assets"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

command -v magick >/dev/null || { echo "ImageMagick (magick) fehlt" >&2; exit 1; }
command -v python3 >/dev/null || { echo "Python 3 fehlt" >&2; exit 1; }

# Icon: direkt aus dem SVG. Die Zeichnung kommt ohne stroke aus, damit auch der
# interne Renderer von ImageMagick sie vollständig darstellt.
magick -background none "$ASSETS/icon.svg" -resize 512x512 -depth 8 "$ASSETS/icon-512.png"
magick -background none "$ASSETS/icon.svg" -resize 256x256 -depth 8 "$ASSETS/icon-256.png"
echo "gebaut: $ASSETS/icon-512.png"
echo "gebaut: $ASSETS/icon-256.png"

# Social Preview: doppelt so groß zeichnen, dann auf die von GitHub erwarteten
# 1280x640 herunterrechnen.
python3 "$ROOT/scripts/social.py" > "$TMP/social.mvg"
magick -size 2560x1280 xc:"#14181d" -draw "@$TMP/social.mvg" \
  \( "$ASSETS/icon-512.png" -resize 232x232 \) -geometry +2152+112 -composite \
  -resize 1280x640 -strip -depth 8 "$ASSETS/social.png"
echo "gebaut: $ASSETS/social.png"
