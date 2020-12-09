# Les 6 - Gegevens uit database

In deze laatste les van de website cursus gaan je leren hoe je gegevens uit de database kan halen. We maken een homepagina voor ons blog met alle posts, gesorteerd op datum met de meest recente posts bovenaan. Om te beginnen moeten we wat code toevoegen aan de _home_ route:

<pre><code class="python">@app.route('/')
def home():
 posts = Post.query.order_by(Post.datum.desc()).all()

 return render_template('home.html', posts=posts)</code></pre>

Zoals je ziet is er een regel toegevoegd waarin we de posts ophalen. Daarnaast zijn de posts doorgevoerd in de _render_template_ functie zodat we ze in het template kunnen gebruiken.

Nu is het tijd om de posts toe te voegen aan de template. Dit doen we met behulp van een loop waarin we door alle posts heen gaan, zodat we de HTML voor een post maar één keer hoeven te schrijven. Ook hier maken we weer gebruik van de stijlen van Bootstrap:

<pre><code class="html">{% extends 'base.html' %}
{% set title = 'Homepagina - Blog' %}

{% block content %}
  &lt;div class=&quot;row&quot;&gt;
    &lt;div class=&quot;col-md-8&quot;&gt;
      {% if posts %}
        {% for post in posts %}
          &lt;div class=&quot;card w-100 mb-2&quot;&gt;
            &lt;div class=&quot;card-body&quot;&gt;
              {% if post.titel %}&lt;h5 class=&quot;card-title&quot;&gt;{{ post.titel }}&lt;/h5&gt;{% endif %}
              &lt;h6 class=&quot;card-subtitle mb-2 text-muted&quot;&gt;{{ post.auteur }} - {{ post.datum.strftime('%Y-%m-%d') }}&lt;/h6&gt;
              &lt;p class=&quot;card-text&quot;&gt;{{ post.content }}&lt;/p&gt;
            &lt;/div&gt;
          &lt;/div&gt;
        {% endfor %}
      {% endif %}
    &lt;/div&gt;

    &lt;!-- sidebar --&gt;
    &lt;div class=&quot;col-md-4&quot;&gt;
      &lt;div class=&quot;card w-100&quot;&gt;
        &lt;div class=&quot;card-header&quot;&gt; Featured &lt;/div&gt;
        &lt;ul class=&quot;list-group list-group-flush&quot;&gt;
          &lt;li class=&quot;list-group-item&quot;&gt;Cras justo odio&lt;/li&gt;
          &lt;li class=&quot;list-group-item&quot;&gt;Dapibus ac facilisis in&lt;/li&gt;
          &lt;li class=&quot;list-group-item&quot;&gt;Vestibulum at eros&lt;/li&gt;
        &lt;/ul&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  &lt;/div&gt;
{% endblock %}</code></pre>

Zoals je ziet hebben we eerst een _if_-statement toegevoegd, die controleert of er wel posts bestaan, en daarna is er een loop toegevoegd. Deze loop gaat door alle posts heen en geeft de data uit de posts goed weer. Omdat een titel voor een post niet verplicht is, is er een _if_-statement om de titel-variabele toegevoegd. Als deze er niet is, zou er soms een lege titel-tag voorkomen.

Dit was het einde van de website cursus. Nog veel succes met het verder ontwikkelen van websites met Python en Flask!