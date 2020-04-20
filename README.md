Das Repo behinhaltet meine Lösung zur gestellten Tech4Germany Codechallenge.

### How to run

Das Repo ist als standard python module mit setup file aufgebaut. Es kann somit über einen einfachen 
pip install command installiert werden.

```
git clone https://github.com/wbglaeser/t4g-cchallenge.git

pip install -r requirements.txt
``` 

Die App wird mit einem einfachen python command gestartet und läuft auf dem localhost und unter dem Port 5000.

```
python app.py
```

Die Pegelstände befinden sich auf folgender URL:
```
http://localhost:5000/water_levels
```

#### Comments

In der Liste der Stationen habe ich für Passau tatsächlich vier Messstation finden können. Zwei von diesen
geben aber, soweit ich es verstehe, eine Durchfahrtshöhe an und damit nur indirekt den Pegelstand. Bei einer kurzen
Internetrecherche habe ich tatsächlich noch weitere Station finden können [here]("https://www.hnd.bayern.de/pegel/meldestufen/donau_bis_passau").
Diese Stationen habe ich aber nicht in der API finden können. Daher habe die Messstationen für die
Durchfahrtshöhe mit eigebaut, auf eine Angabe der Meldestufe hier aber verzichtet. Wahrscheinlich habe
ich die anderen zwei Messtationen übersehen.
