# Mitarbeit

Hinweise, Korrekturen und Ergänzungen sind willkommen – besonders zu Rechtslage und Gremienpraxis in Österreich und der Schweiz, die hier dünner ausfällt als der deutsche Teil.

## Issue oder Pull Request

Bei kleinen Korrekturen – Tippfehler, falscher Paragraf, toter Link – gern direkt einen Pull Request. Bei allem, was die Struktur des Skills betrifft, vorher ein Issue mit dem Vorschlag.

## Was beim Ändern von `SKILL.md` gilt

- **Kurz halten.** Der Skill wird bei jeder Nutzung in den Kontext geladen. Jeder Satz muss das Verhalten ändern, sonst kommt er raus.
- **Ausführliches in `references/`.** Dort liegt, was nur bei Bedarf gebraucht wird.
- **Deutsch nach den Regeln im Skill selbst:** Siezen, deutsche Anführungszeichen „so“, Halbgeviertstrich mit Leerzeichen ( – ), kein Beraterdenglisch, kein Nominalstil.
- **Kein Rechtsrat.** Rechtsbezüge sind Prüfpunkte, keine Auskunft. Formulierungen, die nach verbindlicher Beratung klingen, werden abgelehnt.
- **Paragrafen belegen.** Wer eine Norm ergänzt, nennt Gesetz, Paragraf und Anwendungsfall in einem Satz.
- **Checkliste nachziehen.** Eine neue Regel ohne Eintrag in der Checkliste wird nicht befolgt.
- **Version anheben.** Das Feld `metadata.version` im Frontmatter folgt dem Schema `JJJJ.M.T`, `version` in `.claude-plugin/plugin.json` und `marketplace.json` folgt Semantic Versioning. Beides eintragen, dazu eine Zeile in `CHANGELOG.md`.

## Prüfen vor dem Absenden

Der Skill lässt sich nicht automatisch testen. Stattdessen von Hand:

1. Skill lokal nach `~/.claude/skills/sechs-perspektiven/` kopieren, Claude Code neu starten.
2. Eine echte Frage stellen und prüfen, ob der Skill greift.
3. Die Checkliste aus `SKILL.md` am Ergebnis durchgehen.
4. Mindestens einen Durchlauf im Modus **Vorlage** und einen im Modus **Workshop**.

## Lizenz

Beiträge stehen unter der MIT-Lizenz dieses Repositorys. Wer Text aus anderen Quellen übernimmt, nennt sie in [CREDITS.md](CREDITS.md) und prüft, ob die Lizenz das zulässt.
