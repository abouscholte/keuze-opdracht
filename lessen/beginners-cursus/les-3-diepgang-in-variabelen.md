# Les 3 - Diepgang in variabelen

Wanneer er specifieker gekeken wordt naar de variabelen wordt het al snel duidelijk dat deze waardes niet vast staan. Op het moment dat een variabelen namelijk wordt ingevoerd, kan hij daarna nog door middel van een andere functie veranderd worden. 

Verder zitten er strikte regels verbonden aan de benaming van variabelen:
- De naam van een variabele moet starten met een letter of een laag streepje;
- De naam kan niet starten met een nummer;
- De letters kunnen alleen uit het europese alfabet komen;
- De namen van variabelen zijn gevoelig voor hoofdletters en kleine letters.

<pre><code class="python">myvar = "Iva"
my_var = "Iva"
_my_var = "Iva"</code></pre>

Aangezien sommigen van deze namen uit meer dan 1 woord bestaan is het soms handig om voor elk nieuwe woord een hoofdletter te gebruiken, of om een laag streepje na elk woord te zetten.

Verder is het ook mogelijk in Python om meerdere variabelen in een regel te creëren. Dit kan door ze naast elkaar te zetten m.b.v. komma’s:

<pre><code class="python">a, b, c = "Iva", "Alain", "Lieke"

print(a)
print(b)
print(c)</code></pre>

Wanneer deze code uitgevoerd zou worden door Python zou er dus het volgende staan:

<pre><code class="python">Iva
Alain
Lieke</code></pre>

Ook kan je meerdere variabelen dezelfde waarde geven door een _=_ tussen de variabelen te plaatsen:

<pre><code class="python">a = b = c = “Wij zijn enorm goed in informatica”</code></pre>

Om een variabele en een tekst te printen gebruikt Python een _+_ symbool:

<pre><code class="python">x = "geweldig"
print("Informatica is " + x)</code></pre>

Wanneer dit wordt gedaan met nummers wordt het programma als het ware een rekenmachine en wordt de ingevoerde som berekend:

<pre><code class="python">x = 5
y = 10
print(x + y)</code></pre>

De output is dan in dit geval 15.

In de volgende les gaan we kijken naar verschillende soorten data en nummers in Python.