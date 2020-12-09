# Les 5 - Databasebeheer met Python

In deze les gaan we een database aanmaken waarin we alle posts kunnen opslaan die worden aangemaakt. We maken deze database met behulp van de Flask-_library_ SQLAlchemy. SQLAlchemy is een tool die ervoor zorgt dat we met gemak een databasemodel aan kunnen maken en die daarna kunnen beheren via de Terminal of Command Line. We gebruiken een SQLite database die gebruik maakt van een enkel bestand. Dit bestand gaat _blog.db_ heten en dit bestand wordt automatisch gegenereerd door SQLAlchemy.

Als eerste moeten we SQLAlchemy installeren. We gebruiken de versie die speciaal is gemaakt voor Flask. Dit doen we zo:

<pre><code class="bash">$ pip install flask-sqlalchemy</code></pre>

Dit installeert alles dat nodig is voor SQLAlchemy. Nu kunnen we in \__init__.py een databasemodel aanmaken waarin de posts kunnen worden vermeld. Voeg daarna deze code toe:

<pre><code class="python">from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)


# database model

class Post(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 titel = db.Column(db.String(500), nullable=True)
 content = db.Column(db.Text, nullable=False)
 auteur = db.Column(db.String(500), nullable=False)
 datum = db.Column(db.DateTime, nullable=False)</code></pre>

De eerste regel (die normaal gesproken helemaal bovenin het bestand komt te staan), importeert SQLAlchemy. In de regel daarna (die bij de andere app.config komt te staan) stellen we de locatie voor ons database bestand in. Daarna stellen we de database in als een SQLAlchemy database. Hieraan voegen we onze app variabele toe zodat Flask weet dat de database bij deze app hoort. Onderaan maken we ons model aan.

Eerst zie je dat het model wordt opgesteld met behulp van een Python _class_. De class geven we de naam Post en dit is een database model. De eerste regel is de _id_ van het model. Dit is ook de primary key. Daarna stellen we de titel, de content, de auteur en de datum op. Let op dat er soms een String wordt gebruikt (met een maximale waarde van 500 karakters) en soms een Text wordt gebruikt. Let ook op de _nullable_ die steeds wordt weergegeven. Dit geeft aan of er een lege waarde mag bestaan. Als dit _False_ is, betekent het dat er geen lege waarde mag bestaan.

Nu de database is opgesteld, is het tijd om de database ook daadwerkelijk aan te maken. Dit doen we weer in de Terminal of Command Line. Open eerst een Python venster in de juiste map met het _virtual environment_ ingeschakeld. Voer dan dit commando uit als je Mac gebruikt:

<pre><code class="bash">$ python</code></pre>

Op Windows moet je dit intypen:

<pre><code class="bash">> py -3</code></pre>

Nu is het Python venster geopend en kan je commando’s uitvoeren op je project. We gaan dus onze database aanmaken. Dit doen we zo:

<pre><code class="python">>>> from blog import db
>>> db.create_all()</pre></code>

Er kan een waarschuwing optreden na het schrijven van de eerste regel. Dit is niet erg en kun je negeren. Als je deze twee commando’s hebt uitgevoerd, moet je een nieuw bestand in je blog map zien: _blog.db_. Dit is onze database. Het laatste dat we nu nog moeten doen is de mogelijkheid toevoegen om posts toe te voegen. Dit doen we door de _nieuwe_post_ route aan te passen. Deze zal er nu zo uitzien:

<pre><code class="python">@app.route('/nieuwe-post/', methods=['GET', 'POST'])
def nieuwe_post():
 form = NieuwePostFormulier()

 if form.validate_on_submit():
   post = Post(titel=form.titel.data, content=form.content.data, auteur=form.auteur.data,
               datum=datetime.now())
   db.session.add(post)
   db.session.commit()

   return redirect(url_for('home'))

 return render_template('nieuwe-post.html', form=form)</code></pre>

Als nu het formulier wordt ingevuld, wordt er een Post opgesteld met de juiste data uit het formulier. Deze post wordt dan toegevoegd en daarna wordt de sessie naar de database gestuurd. Uiteindelijk worden we met de _redirect_ functie, ingebouwd in Flask, weer terug gestuurd naar de homepagina. De _url_for_ functie gebruikt de naam van de route om de juiste pagina te vinden. Het enige dat we nog moeten doen is de nieuwe functies importeren. Dit doen we zo:

<pre><code class="python">from datetime import datetime

from flask import Flask, render_template, redirect, url_for</code></pre>

Deze twee regels staan bovenin het bestand. Om te controleren of de gegevens daadwerkelijk in de database staan, kan je in je Terminal of Command Line, in een Python venster de database gegevens importeren. Dit doe je zo:

<pre><code class="python">>>> from blog import Post
>>> post = Post.query.first()
>>> post
<Post 1>
>>> post.content
'Dit is hele mooie content!'</code></pre>

Eerst importeren we het Post model. Daarna stellen we een variabele op die de eerste post inhoudt van het Post model. Deze post kunnen we weergeven en we kunnen ook de content van deze post weergeven.

Nu heb je de kennis om elk soort database aan te maken met Flask. Het is dus erg gemakkelijk en snel om hiermee te starten. In de volgende en laatste les leren we hoe we de posts op kunnen halen uit de database en te tonen op de homepagina.