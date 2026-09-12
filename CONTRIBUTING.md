# Mitmachen

Dieser Skill lebt von Runden, die schiefgegangen sind, und von Prüfpunkten, die jemand aus der eigenen Praxis kennt. Beides ist willkommen.

## Was besonders hilft

**Eine schwache Runde.** Der Skill hat Perspektiven vermischt, ein Risiko ohne Gegenmaßnahme durchgelassen, eine Zahl ohne Quelle als `[BELEGT]` geführt oder eine Empfehlung abgegeben, die in den Perspektiven davor nicht vorkam. Leitfrage, Modus und die betroffene Passage genügen – die ganze Antwort braucht niemand.

**Ein fehlender DACH-Prüfpunkt.** Eine Mitbestimmungs-, Datenschutz-, Aufsichts- oder Vergabefrage, die in `references/dach-pruefpunkte.md` fehlt. Nützlich sind Punkte, die man leicht übersieht und die spät teuer werden. Was ohnehin jede Beraterin im Kopf hat, bläht die Datei nur auf.

**Eine bessere Beschlussvorlage.** Die Gliederung im Modus *Vorlage* ist ein Vorschlag. Wer weiß, wie Sitzungsunterlagen in Aufsichtsrat, Verwaltungsrat oder Personalausschuss tatsächlich aussehen müssen, möge widersprechen.

Für die ersten beiden Fälle gibt es [Issue-Vorlagen](https://github.com/m-dohmen/sechs-perspektiven/issues/new/choose). Alles andere als freies Issue.

## Änderungen am Skill

`skills/sechs-perspektiven/SKILL.md` ist der Kern und soll knapp bleiben. Er wird bei jedem Aufruf vollständig gelesen – jede Zeile kostet Kontext, den die eigentliche Analyse dann nicht mehr hat.

- **Regeln gehören in `SKILL.md`, Belege in `references/`.** Eine neue Regel ist ein Satz. Begründung, Fundstelle und Beispiele wandern in eine Referenzdatei.
- **Jede neue Regel bekommt einen Eintrag in der Checkliste** am Ende von `SKILL.md`. Was dort nicht steht, prüft der Skill am Ende nicht nach.
- **Rechtsbezüge nennen Gesetz, Paragraf und Anwendungsfall** und sind als Prüfpunkt formuliert, nicht als Auskunft. „Prüfen, ob § 87 Abs. 1 Nr. 6 BetrVG greift“ ist richtig, „ist mitbestimmungspflichtig“ ist falsch – das entscheidet der Einzelfall.
- **Pflichtformate nicht aufweichen.** Risiko ohne Gegenmaßnahme, Nutzen ohne Bedingung, Fakt ohne Beleg-Marker: Genau diese drei Fesseln unterscheiden eine Runde von einer Aufzählung.
- **Deutsch ohne Beraterdenglisch.** Siezen, deutsche Anführungszeichen „so“, Halbgeviertstrich mit Leerzeichen ( – ), nie der englische Geviertstrich. Die Gegenprobe: `grep -rc '—' skills/sechs-perspektiven/` muss überall `0` liefern.

## Ausprobieren

Es gibt keine Testsuite – der Skill ist Prosa. Geprüft wird von Hand:

```bash
npx skills add . -y        # lokalen Stand installieren
./scripts/build.sh         # ZIP für Cowork, claude.ai und Codex bauen
```

Dann mindestens eine echte Leitfrage durchspielen, davon einen Durchlauf im Modus **Vorlage** – dort zeigt sich am schnellsten, ob Synthese und Beschlussvorlage noch zusammenpassen. Prüfen:

- Jede Perspektive hält ihr Pflichtformat ein.
- Weiß erfindet keine Zahlen; Fehlendes steht als `[OFFEN]` und taucht in der Vorlage wieder auf.
- Die Synthese führt nichts ein, was vorher nicht dastand.
- Die DACH-Prüfpunkte tauchen nur auf, wenn sie zur Leitfrage passen, und nicht als Pflichtabsatz.

## Pull Requests

Ein Thema pro Pull Request. Im Text kurz sagen, welches Problem die Änderung löst – eine Leitfrage, an der man es nachvollziehen kann, sagt oft mehr als eine Beschreibung.

Ändert sich der Skill inhaltlich, die Version an drei Stellen nachziehen – `SKILL.md` (Feld `metadata.version`), `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` – und eine Zeile in `CHANGELOG.md` ergänzen.

## Verhaltenskodex

Für dieses Projekt gilt der [Verhaltenskodex](CODE_OF_CONDUCT.md).

## Lizenz

Beiträge stehen unter MIT, wie das übrige Projekt.
