# Les 3 - Je eerste webpagina met Flask

Nu je Flask en Python hebt geïnstalleerd, en je je systeem al voor een deel hebt klaargezet, is het nu echt tijd om een website te gaan maken! We gaan een simpel blog maken waarin iedereen nieuwe posts kan toevoegen die ook aan een database worden toegevoegd. In deze uitleg komen alle beginselen aan bod die nuttig zijn voor elk project met Flask.

Om te beginnen, open de map _learning_python_ die we de vorige les hebben aangemaakt in je favoriete teksteditor, zoals Atom, Visual Studio Code of Notepad++. In deze map zou nu al een map moeten staan met de naam _venv_. Zo niet, ga dan terug naar de vorige les. Deze map gaan we niet gebruiken maar is wel belangrijk voor het installeren van nieuwe packages en andere functies die nodig zullen zijn voor het project. Vandaar is het belangrijk dat je virtuele omgeving altijd is geactiveerd. Als dit nog niet is, kijk dan in de vorige les hoe dit moest. 

Om alles zo overzichtelijk mogelijk te houden, gaan we ons blog maken in een aparte map, die door Python wordt gezien als een applicatie. Dit doe je door een map aan te maken met de naam _blog_, en daarin een bestand aan te maken met de naam <i>\__init__.py</i>. De naam van de map maakt niet uit, maar omdat we in dit geval een blog maken is dit de meest logische optie. De naam van het bestand is wel belangrijk, want deze naam zorgt ervoor dat Python deze map kan zien als een applicatie. Nu gaan we onze eerste webpagina maken!

In <i>\__init__.py</i>, schrijf de volgende code:

<pre><code class="python">from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
 return 'Hallo Blog!'</code></pre>

In de eerste regel wordt de class Flask geïmporteerd uit de virtuele omgeving. In de tweede regel wordt de app zelf opgesteld. De <i>\__name__</i> variabele in de Flask class is belangrijk om te laten zien dat dit de applicatie zelf is. Daarna wordt de route van de eerste pagina opgesteld. Dit is de homepagina omdat er alleen maar een schuine streep is gebruikt. Flask routes moeten altijd met een schuine streep beginnen. Pagina’s worden altijd opgesteld door middel van een functie, deze eerste functie heet <i>home</i>. De laatste regel geeft aan wat er moet weergegeven worden op de webpagina. Hierin staat voor nu nog alleen maar de tekst ‘Hallo Blog!’. Om deze webpagina ook daadwerkelijk te zien in de webbrowser, voer je de volgende commando’s uit:

<pre><code class="bash">$ export FLASK_APP=blog
$ flask run</code></pre>

Als je Windows gebruikt er verschillende mogelijkheden. Als je _Command Prompt_ gebruikt:

<pre><code class="bash">C:\path\to\app>set FLASK_APP=blog</code></pre>

En als je <i>PowerShell</i> gebruikt:

<pre><code class="bash">PS C:\path\to\app> $env:FLASK_APP = "blog"</code></pre>

Open nu je browser en typ in _localhost:5000_. Nu zou de tekst ‘Hallo Blog!’ zichtbaar moeten zijn. Dit is de manier waarop alle webpagina’s met Flask worden gemaakt. Nu kunnen we in de volgende les complexere webpagina’s maken met behulp van _HTML Templates_ en maken we ons eerste formulier.