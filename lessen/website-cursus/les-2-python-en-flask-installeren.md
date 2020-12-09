# Les 2 - Python en Flask installeren

In deze les wordt uitgelegd hoe je de eerste stappen moet zetten om een website met Python te maken. Hiervoor heb je een juiste versie van Python (3.5 of nieuwer) nodig en het web framework dat we gaan gebruiken in deze cursus, Flask.

Als eerste is het belangrijk om een goede versie van Python geïnstalleerd te hebben op je computer. Ga naar <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a> om de nieuwste versie van Python te installeren op je computer.

Om dan te beginnen met het maken van je project, maak een map aan met de naam _python_website_ op je bureaublad of ergens anders waar je hem makkelijk terug kan vinden. Doe dit met de Terminal op Mac of Command Line op Windows. Dit gaat zo:

<pre><code class="bash">$ cd ~/Desktop/
$ mkdir python_website</code></pre>

Nu is er een map verschenen op je bureaublad. Nu kunnen we met de Terminal of Command Line in die map een _virtual environment_ aanmaken. Dit is een omgeving waarin Python alleen kijkt naar de geïnstalleerde scripts en functies in die virtuele omgeving. Dit is handig omdat als je klaar bent met het project, je makkelijk weer alles kan verwijderen en je kan verschillende versies van functies gebruiken in verschillende projecten. Het wordt altijd aangeraden om een _virtual environment_ te gebruiken bij het maken van een Flask website. Om dit te doen en het meteen te activeren, voer de volgende functies uit:

<pre><code class="bash">$ cd python_website
$ python3 -m venv venv
$ . venv/bin/activate</code></pre>

Op Windows ziet dit er zo uit:

<pre><code class="bash">> cd python_website
> py -3 -m venv venv
> venv\Scripts\activate</code></pre>

Nu zal je in je shell venster zien dat je _virtual environment_ is geactiveerd. Nu kan Flask worden geïnstalleerd. Nadat je dit hebt gedaan, kan je websites bouwen met Flask. Om Flask te installeren, gebruik je de installer Pip die standaard wordt geleverd met Python. Dit gaat zo:

<pre><code class="bash">$ pip install Flask</code></pre>

Nu ben je helemaal klaar om websites te maken met Python en Flask. In de volgende les wordt uitgelegd hoe je een simpele webpagina maakt.