# Les 4 - Data types en nummers

Bij het programmeren is datatype een belangrijk concept. Variabelen kunnen gegevens van verschillende typen opslaan en verschillende typen hebben andere functies. Python heeft standaard de volgende gegevenstypen ingebouwd, in deze categorieën:

<pre><code class="python">Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview</code></pre>

Om uit te vinden onder welke soort gegevenstype een waarde valt, kan je altijd de type() functie gebruiken: 

<pre><code class="python">x = 10
print(type(x))</code></pre>

Hiervan zou de output dan dus ‘int’ zijn aangezien 10 een geheel getal is.

Nu vallen er onder _numeric types_ echter 3 soorten: int, float and complex. Deze staan alle drie voor een ander soort nummer:

<pre><code class="python">x = 8    # int
y = 6.3  # float
z = 2j   # complex</code></pre>

1. Int is een geheel getal, positief of negatief, zonder decimalen, van onbeperkte lengte. 
2. Float, of "drijvend-kommagetal" is een getal, positief of negatief, dat een of meer decimalen bevat (hier kan ook een ‘e’ gebruikt worden om een tot de 10e macht aan de geven).
3. Complexe getallen worden geschreven met een "j" als het imaginaire deel.

Python heeft geen functie random() om een ​​willekeurig getal te maken, maar Python heeft wel een ingebouwde module met de naam random die kan worden gebruikt om willekeurige getallen te maken:

<pre><code class="python">import random

print(random.randrange(2, 7))</code></pre>

Dit was de laatste beginnersles Python. Nu heb je genoeg kennis om door te gaan naar de website cursus, waarin je leert hoe je een dynamische website maakt met behulp van het _web framework_ Flask. Ga <a href="/courses/website/">hier</a> naar die cursus.
