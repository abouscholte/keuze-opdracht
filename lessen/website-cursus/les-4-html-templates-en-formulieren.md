# Les 4 - HTML templates en formulieren

In de vorige les heb je geleerd hoe je een heel simpele webpagina kan maken met Flask. Hierin maakte we gebruik van de return statement en hebben wat tekst laten weergeven in de webbrowser. In plaats van alleen tekst hadden we ook HTML kunnen laten weergeven op de pagina. Dit gaat op dezelfde manier:

<pre><code class="python">return '''&lt;h1&gt;Mijn eerste pagina met Flask!&lt;/h1&gt; 
&lt;p&gt;Welkom op mijn allereerste webpagina gemaakt met Flask en Python!&lt;/p&gt;'''</code></pre>

Dit geeft normale HTML elementen weer op de webpagina. Dit is makkelijk om iets simpels weer te geven, maar niet erg overzichtelijk als je een hele pagina moet schrijven in HTML code. Daarom heeft Flask een functie ingebouwd waarmee HTML bestanden met dynamische elementen kunnen worden ingeladen. Deze functie heet _render_template_ en kan direct uit Flask geïmporteerd worden. Als je dit wilt gebruiken, ziet je python bestand er nu zo uit:

<pre><code class="python">from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('home.html')</code></pre>

In de eerste regel is nu dus een nieuwe functie toegevoegd, om de templates op te halen. Ook is er een verandering gemaakt bij het _return_ statement. Nu wordt de template functie gebruikt om _home.html_ op te halen. _home.html_ is een bestand in de map /blog/templates/ waarop dit staat:

<pre><code class="html">&lt;!DOCTYPE html&gt; 
&lt;html lang=&quot;nl&quot;&gt; 
  &lt;head&gt; 
    &lt;meta charset=&quot;utf-8&quot;&gt; 
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt; 
    
    &lt;title&gt;Mijn eerste webpagina!&lt;/title&gt; 
  &lt;/head&gt;
  
  &lt;body&gt; 
    &lt;h1&gt;Je eerste Flask webpagina!&lt;/h1&gt; 
    &lt;p&gt;Welkom op je allereerste webpagina gemaakt met Python en Flask!&lt;/p&gt; 
  &lt;/body&gt; 
&lt;/html&gt;</code></pre>

Het is verondersteld dat je kennis van HTML goed genoeg is om deze cursus te kunnen volgen. Dit levert een erg simpele webpagina op. Hier willen we wel iets van styling aan toevoegen, maar we willen ook dat op elke pagina op de site bijvoorbeeld dezelfde navigatiebalk te zien is. Dit kunnen we doen met een _base template_. Deze zetten we in dezelfde map als _home.html_ met de naam _base.html_. Dit bestand ziet er nu zo uit:

<pre><code class="html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;nl&quot;&gt;
 &lt;head&gt;
   &lt;meta charset=&quot;utf-8&quot;&gt;
   &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
  
   &lt;title&gt;{% if title %}{{ title }}{% else %}Blog{% endif %}&lt;/title&gt;

   &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css&quot; integrity=&quot;sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2&quot; crossorigin=&quot;anonymous&quot;&gt;
   &lt;link rel=&quot;stylesheet&quot; href=&quot;{{ url_for('static', filename='main.css') }}&quot;&gt;
 &lt;/head&gt;

 &lt;body&gt;
   &lt;nav class=&quot;navbar navbar-expand-lg navbar-light bg-light&quot;&gt;
     &lt;div class=&quot;container container-small&quot;&gt;
       &lt;a class=&quot;navbar-brand&quot; href=&quot;{{ url_for('home') }}&quot;&gt;Blog&lt;/a&gt;
       &lt;button class=&quot;navbar-toggler&quot; type=&quot;button&quot; data-toggle=&quot;collapse&quot; data-target=&quot;#navbarNav&quot; aria-controls=&quot;navbarNav&quot; aria-expanded=&quot;false&quot; aria-label=&quot;Toggle navigation&quot;&gt;
         &lt;span class=&quot;navbar-toggler-icon&quot;&gt;&lt;/span&gt;
       &lt;/button&gt;
       &lt;div class=&quot;collapse navbar-collapse&quot; id=&quot;navbarNav&quot;&gt;
         &lt;ul class=&quot;navbar-nav&quot;&gt;
           &lt;li class=&quot;nav-item&quot;&gt;&lt;a class=&quot;nav-link&quot; href=&quot;{{ url_for('home') }}&quot;&gt;Home&lt;/a&gt;&lt;/li&gt;
           &lt;li class=&quot;nav-item&quot;&gt;&lt;a class=&quot;nav-link&quot; href=&quot;{{ url_for('nieuwe_post') }}&quot;&gt;Nieuwe Post&lt;/a&gt;&lt;/li&gt;
         &lt;/ul&gt;
       &lt;/div&gt;
     &lt;/div&gt;
   &lt;/nav&gt;
  
   &lt;div class=&quot;container container-small container-main&quot;&gt;
     {% block content %}{% endblock %}
   &lt;/div&gt;

   &lt;script src=&quot;https://code.jquery.com/jquery-3.5.1.slim.min.js&quot; integrity=&quot;sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj&quot; crossorigin=&quot;anonymous&quot;&gt;&lt;/script&gt;
   &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js&quot; integrity=&quot;sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx&quot; crossorigin=&quot;anonymous&quot;&gt;&lt;/script&gt;
 &lt;/body&gt;
&lt;/html&gt;</code></pre>

Er is het css-framework Bootstrap toegevoegd voor wat beter ogende styling, samen met een standaard Bootstrap navigatiebalk met een aantal juiste links. Let ook op de _href_ van deze links. Dit zijn speciale template links die gebruikt kunnen worden in Flask. Ze worden verwezen naar de functienaam zoals we die hebben geschreven in <i>\__init__.py</i>. Ook bij het css bestand dat ik heb toegevoegd is deze soort code toegevoegd. Dit css bestand is <a href="https://github.com/abouscholte/python_website/blob/master/blog/static/main.css" target="_blank">hier, op GitHub</a> te downloaden. 

Je zult zien dat er nu een foutmelding zal optreden, omdat er al een _url_for_ is toegevoegd voor de route voor de pagina voor het toevoegen van nieuwe posts. Deze pagina bestaat nog niet, dus dat is begrijpelijk.

Net boven de script tags die gebruikt worden door Bootstrap, staat in een container een block voor de content. Dit is waar de content dus naartoe gaat. Als we dan kijken naar _home.html_, ziet dit er nu zo uit:

<pre><code class="html">{% extends 'base.html' %}
{% set title = 'Homepagina - Blog' %}

{% block content %}
 &lt;h1&gt;Je eerste Flask webpagina!&lt;/h1&gt;
 &lt;p&gt;Welkom op je allereerste webpagina gemaakt met Python en Flask!&lt;/p&gt;
{% endblock %}</code></pre>

Dit is veel simpeler dan eerst, omdat nu alle omliggende code in _base.html_ staat, waar we niet meer naar hoeven te kijken. Dit wordt geregeld door de eerste regel. De tweede regel stelt een variabele in voor de titel, die wordt weergegeven in _base.html_ in de _title_-tag. Nu gaan we ook nog een pagina aanmaken waarin we het formulier gaan toevoegen. Eerst gaan we dit formulier maken met een bepaalde _library_ in Flask die het ons heel makkelijk maakt om formulieren aan te maken, genaamd _Flask-WTF_. Om dit te installeren, typ:

<pre><code class="bash">$ pip install flask-wtf</code></pre>

Maak nu een nieuw bestand aan met de naam <i>forms.py</i> in de blog map. Hierin komt je formulier te staan. We gaan een formulier maken waarin gebruikers een nieuwe post kunnen aanmaken. Hierin moet dus een titel, content en de naam van de auteur komen te staan. Deze velden hebben we dus nodig in het formulier. Dit doen we zo:

<pre><code class="python">from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class NieuwePostFormulier(FlaskForm):
 titel = StringField('Voeg een titel toe aan je post', validators=[DataRequired()])
 content = TextAreaField('Voeg content toe aan je post', validators=[DataRequired()])
 auteur = StringField('Vul je naam in', validators=[DataRequired()])
 submit = SubmitField('Voeg toe')</code></pre>

Wat er hier gebeurt, is dat het formulier wordt opgesteld door een class te gebruiken. Hierin staan alle velden apart aangegeven met de correcte soort invulveld. Zo is er een StringField, TextAreaField en een SubmitField. Deze worden zo erg duidelijk als we dit om gaan zetten in HTML. We moeten eerst nog alleen dit formulier importeren in <i>\__init__.py</i>. Dit doen we door aan de bovenkant van de pagina, net onder het importeren van Flask zelf, dit te typen:

<pre><code class="python">from blog.forms import NieuwePostFormulier</code></pre>

Nu kunnen we een nieuwe route aanmaken waarin dat formulier wordt vermeld:

<pre><code class="python">@app.route('/nieuwe-post/', methods=['GET', 'POST'])
def nieuwe_post():
 form = NieuwePostFormulier()
  return render_template('nieuwe-post.html', form=form)</code></pre>

Nu moeten we alleen nog een nieuw template aanmaken met de naam _nieuwe-post.html_. Daarin verwerken we het formulier met template code, zoals eerder al gezien in _base.html_.

<pre><code class="html">{% extends 'base.html' %}
{% set title = 'Nieuwe Post' %}

{% block content %}
 &lt;form action=&quot;&quot; method=&quot;POST&quot;&gt;
   {{ form.csrf_token }}
   &lt;div class=&quot;form-group&quot;&gt;
     {{ form.titel.label }}
     {% if form.titel.errors %}
       {{ form.titel(class=&quot;form-control&quot;) }}
       {% for error in form.titel.errors %}
         &lt;div class=&quot;invalid-feedback&quot;&gt;{{ error }}&lt;/div&gt;
       {% endfor %}
     {% else %}
       {{ form.titel(class=&quot;form-control&quot;) }}
     {% endif %}
   &lt;/div&gt;
   &lt;div class=&quot;form-group&quot;&gt;
     {{ form.content.label }}
     {% if form.content.errors %}
       {{ form.content(class=&quot;form-control&quot;) }}
       {% for error in form.content.errors %}
         &lt;div class=&quot;invalid-feedback&quot;&gt;{{ error }}&lt;/div&gt;
       {% endfor %}
     {% else %}
       {{ form.content(class=&quot;form-control&quot;) }}
     {% endif %}
   &lt;/div&gt;
   &lt;div class=&quot;form-group&quot;&gt;
     {{ form.auteur.label }}
     {% if form.auteur.errors %}
       {{ form.auteur(class=&quot;form-control&quot;) }}
       {% for error in form.auteur.errors %}
         &lt;div class=&quot;invalid-feedback&quot;&gt;{{ error }}&lt;/div&gt;
       {% endfor %}
     {% else %}
       {{ form.auteur(class=&quot;form-control&quot;) }}
     {% endif %}
   &lt;/div&gt;
   {{ form.submit(class=&quot;btn btn-primary&quot;) }}
 &lt;/form&gt;
{% endblock %}</code></pre>

Je ziet dat in elke _form-group_, er eerst een label wordt neergezet. Daarna wordt er gecontroleerd of er voor dat bepaalde veld foutmeldingen zijn. Als die er wel zijn, krijgt eerst de input zelf een class van _is-invalid_, en daarna komt er ook nog een stuk tekst voor de _invalid-feedback_. Als er niks fout is gegaan, wordt er alleen maar een normale input weergegeven. Alle classes die worden gebruikt zijn van Bootstrap en zijn dus heel makkelijk in gebruik. 

Als je de pagina nu wilt openen, zul je een foutmelding zien dat er een _Secret Key_ nodig is. Deze voegen we toe op deze manier aan <i>\__init__.py</i>:

<pre><code class="python">app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyz'</code></pre>

Deze regel komt na de regel waarin we Flask instellen als de applicatie. Wat er binnen de string staat zou alles kunnen zijn, maar het beste is om een zo willekeurig mogelijke volgorde van letters en nummers te gebruiken. Het alfabet, zoals hier, is niet heel veilig.

Nu kunnen we wel de pagina openen in de webbrowser en ons nieuwe formulier bekijken. Hij is nog niet bruikbaar, maar ziet er al wel mooi uit!