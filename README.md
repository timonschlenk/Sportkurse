# Sportkurse Bot

## Installation
Befolge folgende Schritte:

1. Installiere eine aktuelle Version von Python
2. Installiere Selenium, gebe dafür ins Terminal ein:
```terminal
pip install selenium
```
3. Installiere eine aktuelle Version von Google Chrome oder Firefox und den dazugehörigen Driver ([Chrome](https://sites.google.com/chromium.org/driver/), [Firefox](https://github.com/mozilla/geckodriver))
4. Kopiere die Executable des Drivers in den root Ordner des Projekts und benenne sie ``` chromedriver.exe ``` bzw. ``` geckodriver.exe ```
5. Füge eine ``` data.json ``` Datei in den Root Ordner hinzu in welcher sich private Informationen für die Anmeldung befinden. Es folgt ein Beispiel
```json
[
    {
        "LINK": "https://www.dhsz.tu-dresden.de/angebote/aktueller_zeitraum/_Tischtennis_ABS.html",
        "KURSNUMMER": "AB1504128",
        "VORNAME": "Max", 
        "NAME": "Mustermann", 
        "STRASSE": "Musterstraße 1", 
        "ORT": "01234 Bielefeld", 
        "GEBURTSDATUM": "01.01.2000", 
        "STATUS": "Stud. TU Dresden", 
        "MATNR": "1234567", 
        "EMAIL": "max@mustermann.de"
    },
    {
        "LINK": "https://www.dhsz.tu-dresden.de/angebote/aktueller_zeitraum/_Tischtennis_ABS.html",
        "KURSNUMMER": "AB1504128",
        "VORNAME": "Marla", 
        "NAME": "Mustermann", 
        "STRASSE": "Musterstraße 1", 
        "ORT": "01234 Bielefeld", 
        "GEBURTSDATUM": "01.01.2000", 
        "STATUS": "Stud. TU Dresden", 
        "MATNR": "1234567", 
        "EMAIL": "marla@mustermann.de"
    }
]
```
6. Habe Spaß an den Sportkursen xD

## Ausführung
Einfach Skript ausführen, dann laden die Seiten der Sportkurse automatisch und refreshen solange bis der Anmeldebutton erscheint, anschließend werden die Informationen automatisiert eingegeben und man muss nur noch auf Buchung bestätigen klicken
