#!/usr/bin/env python3
"""Schreibt die MVG-Zeichenanweisungen für assets/social.png nach stdout.

ImageMagick rendert daraus das Social Preview. Der Weg über MVG statt über
einen Browser hält den Bau deterministisch und ohne Chrome.
"""

S = 2  # Renderfaktor, danach auf 1280x640 heruntergerechnet
W, H, PAD = 1280, 640, 88

BG = "#14181d"
KARTE = "#1a1f26"
LINIE = "#2a2f36"
HELL = "#f4f1ea"
GRAU = "#8b8579"

BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
REG = "/System/Library/Fonts/Helvetica.ttc"

KARTEN = [
    ("#3f86c8", "Blau", "Steuerung"),
    ("#f4f1ea", "Weiß", "Fakten"),
    ("#e2564d", "Rot", "Gefühl"),
    (None, "Schwarz", "Risiko"),
    ("#e8b13a", "Gelb", "Nutzen"),
    ("#4a9e6a", "Grün", "Kreativität"),
]

out = []
a = out.append


def p(v):
    return v * S


a('push graphic-context')
a(f'fill "{BG}" rectangle 0,0 {p(W)},{p(H)}')

# Titel
a(f'font "{BOLD}" font-weight 700 font-size {p(76)} fill "{HELL}"')
a(f'text {p(PAD)},{p(150)} "Sechs Perspektiven"')

# Claim
a(f'font "{REG}" font-weight 400 font-size {p(27)} fill "{GRAU}"')
a(f'text {p(PAD)},{p(208)} "Die Denkhüte von de Bono, auf Deutsch – '
  f'für Beratung, Gremien und Workshops."')

# Trennlinie
a(f'fill "{LINIE}" rectangle {p(PAD)},{p(272)} {p(W - PAD)},{p(273)}')

# Karten
n = len(KARTEN)
gap = 18
breite = (W - 2 * PAD - gap * (n - 1)) / n
oben, unten = 330, 500
for i, (farbe, name, rolle) in enumerate(KARTEN):
    x = PAD + i * (breite + gap)
    a(f'fill "{KARTE}" stroke "{LINIE}" stroke-width {p(1)} '
      f'roundrectangle {p(x)},{p(oben)} {p(x + breite)},{p(unten)} {p(14)},{p(14)}')
    a('stroke none')
    cx, cy, r = x + 30, oben + 44, 11
    if farbe is None:  # Schwarz als Ring, damit er auf dunklem Grund sichtbar ist
        a(f'fill "{HELL}" circle {p(cx)},{p(cy)} {p(cx + r)},{p(cy)}')
        a(f'fill "{KARTE}" circle {p(cx)},{p(cy)} {p(cx + r - 3)},{p(cy)}')
    else:
        a(f'fill "{farbe}" circle {p(cx)},{p(cy)} {p(cx + r)},{p(cy)}')
    a(f'font "{BOLD}" font-weight 700 font-size {p(24)} fill "{HELL}"')
    a(f'text {p(x + 19)},{p(oben + 100)} "{name}"')
    a(f'font "{REG}" font-weight 400 font-size {p(20)} fill "{GRAU}"')
    a(f'text {p(x + 19)},{p(oben + 134)} "{rolle}"')

# Fußzeile
a(f'font "{REG}" font-weight 600 font-size {p(21)} fill "{GRAU}"')
a(f'text {p(PAD)},{p(570)} "Claude Code · Cowork · Codex CLI · API"')
a('text-align right')
a(f'text {p(W - PAD)},{p(570)} "github.com/m-dohmen/sechs-perspektiven"')

a('pop graphic-context')
print("\n".join(out))
