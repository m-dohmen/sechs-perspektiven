# Sechs Perspektiven

Ein Agent Skill für Claude Code: die Denkhüte von Edward de Bono auf Deutsch, zugeschnitten auf Beratung, Gremienarbeit und Workshops im DACH-Raum.

Statt Fakten, Gefühl, Risiko und Zuversicht in einer vermischten Antwort zu liefern, arbeitet Claude sechs Rollen nacheinander ab – alle jeweils in derselben Rolle. Am Ende steht eine Synthese, die nur zusammenzieht, was die Perspektiven ergeben haben.

## Was anders ist als im englischen Original

- **Durchgängig Deutsch**, Siezen als Standard, deutsche Typografie, kein Beraterdenglisch
- **DACH-Prüfpunkte:** Mitbestimmung (BetrVG, ArbVG, Mitwirkungsgesetz), DSGVO und revDSG, EU AI Act, NIS2, DORA, MaRisk, Vergaberecht, Aufsicht durch BaFin, FMA und FINMA
- **Modus „Vorlage“:** hängt eine fertige Beschlussvorlage an – Sachverhalt, Entscheidungsbedarf, Optionen, Empfehlung, Mittel und Termine, offene Punkte
- **Modus „Workshop“:** getaktete Moderation für eine Runde mit mehreren Personen, inklusive Umgang mit Rangdynamik
- **Adressat im Startblock:** Vorstand, Lenkungsausschuss oder Fachbereich steuern Tonlage und Detailgrad
- **Strengere Beweisregel:** Zahlen ohne Quelle gelten als Annahme oder offener Punkt, nie als belegt
- **Risikoeinstufung** nach Eintritt und Wirkung in der Tiefe „Tief“
- **Drei Referenzdateien:** durchgespielte Beispielsitzung, DACH-Prüfpunkte, Moderationsleitfaden

## Installation

### Als Plugin über das Marketplace-Verzeichnis

```
/plugin marketplace add m-dohmen/sechs-perspektiven
/plugin install sechs-perspektiven@sechs-perspektiven
```

### Als einzelner Skill

```bash
git clone https://github.com/m-dohmen/sechs-perspektiven.git
cp -r sechs-perspektiven/skills/sechs-perspektiven ~/.claude/skills/
```

Projektweit statt benutzerweit: nach `.claude/skills/` im Projektverzeichnis kopieren.

Danach Claude Code neu starten. Mit `/plugin` bzw. über die Skill-Liste prüfen, ob der Skill geladen ist.

## Verwendung

Der Skill greift von selbst, sobald eine Anfrage danach klingt:

```
Sechs Perspektiven zu der Frage, ob wir die Rechnungsverarbeitung
auf ein KI-System umstellen.
```

```
Mach mir dazu eine Entscheidungsvorlage nach den Denkhüten,
Adressat ist die Geschäftsführung.
```

Modus und Tiefe lassen sich mitgeben:

```
Sechs Perspektiven, Modus Risiko, Tiefe tief:
Auslagerung des Rechenzentrumsbetriebs an einen Anbieter in Irland.
```

| Modus | Reihenfolge | Wofür |
|-------|-------------|-------|
| Vollbild (Standard) | Blau → Weiß → Rot → Schwarz → Gelb → Grün → Blau | Breite Entscheidungen |
| Kreativ | Blau → Grün → Gelb → Rot → Blau | Ideenfindung |
| Risiko | Blau → Weiß → Schwarz → Blau | Risikodurchsicht |
| Entscheidung | Blau → Weiß → Schwarz → Gelb → Blau | Go/No-Go |
| Vorlage | wie Entscheidung, plus Beschlussvorlage | Gremiensitzung |
| Workshop | frei, Blau am Schluss | Moderierte Runde |
| Frei | selbst gewählt + Blau | eigene Zusammenstellung |

Tiefe: **Kurz** (2 Punkte je Perspektive), **Standard** (3), **Tief** (4–5 plus Risikoeinstufung).

## Die sechs Perspektiven

| | Rolle | Inhalt |
|---|-------|--------|
| 🔵 | Blau | Steuerung: rahmt zu Beginn, führt am Ende zusammen |
| ⚪ | Weiß | Fakten, jeweils als belegt, Annahme oder offen markiert |
| 🔴 | Rot | Gefühl und Intuition, ohne Begründungspflicht |
| ⚫ | Schwarz | Risiken, jedes mit Gegenmaßnahme |
| 🟡 | Gelb | Nutzen, jeder mit Bedingung |
| 🟢 | Grün | Alternativen, ohne Bewertung |

## Aufbau des Repositorys

```
.
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
└── skills/
    └── sechs-perspektiven/
        ├── SKILL.md
        └── references/
            ├── beispielsitzung.md
            ├── dach-pruefpunkte.md
            └── moderation.md
```

## Hinweis

Die DACH-Prüfpunkte sind eine Gedächtnisstütze, kein Rechtsrat. Rechtsfragen gehören zu Justiziariat oder Kanzlei; der Skill macht sie sichtbar, er klärt sie nicht.

## Herkunft und Dank

Diese Fassung baut auf dem Skill [six-thinking-hats](https://github.com/ysskrishna/ai-agent-skills/tree/main/skills/six-thinking-hats) von **[ysskrishna](https://github.com/ysskrishna)** auf, veröffentlicht unter MIT-Lizenz. Aufbau, Modi, Tiefenstufen und die Trennung von Perspektive und Synthese stammen von dort. Danke an ysskrishna für die Vorarbeit und dafür, sie offen geteilt zu haben.

Die Methode selbst geht auf **Edward de Bono**, *Six Thinking Hats* (1985), zurück.

Einzelheiten zur Abgrenzung stehen in [CREDITS.md](CREDITS.md).

## Mitarbeit

Hinweise und Korrekturen gern als Issue oder Pull Request – siehe [CONTRIBUTING.md](CONTRIBUTING.md).

## Lizenz

MIT, siehe [LICENSE](LICENSE) und [NOTICE](NOTICE).
