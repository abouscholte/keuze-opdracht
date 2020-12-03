# Les 1 - Beginnen met Python

Welkom bij het leren van Python. Python is een populaire programmeertaal die veel wordt gebruikt als server taal bij webapplicaties, zoals Netflix of Instagram. Python is bedacht en gemaakt door Nederlander Guido van Rossum in 1991.

Naast het gebruik van Python in websites, wordt de taal ook veel gebruikt voor wiskundige problemen en data science. In deze eerste cursus wordt er nog alleen maar gekeken naar de beginselen van de programmeertaal, waardoor je een beter begrip krijgt van de makkelijke syntax, die lijkt op normaal Engels.

## De syntax van Python

Om te beginnen met coderen in Python, moet je eerst weten hoe een Python bestand eruit kan zien. In veel programmeertalen worden accolades, haakjes en puntkomma’s gebruikt om verschillende commando’s aan te geven. In Python wordt er alleen gebruik gemaakt van nieuwe regels en inspringingen. Hieronder is een simpel Python bestand te zien:

<pre><code class="python">def myFunc(firstName, lastName):
	name = firstName + ' ' + lastName
	print(name)

myFunc('Jan', 'de Jong')
</code></pre>

In dit stukje code wordt eerst een functie opgesteld met de naam _myFunc_. In die functie komen twee variabelen voor: _firstName_ en _lastName_. Deze variabelen moet je opgeven als je de functie wilt gebruiken. Uit deze voor- en achternaam wordt dan een volledige naam gemaakt, met een spatie ertussen. Daarna wordt de naam geprint op het scherm.

In de laatste regel wordt de functie uitgevoerd, met de naam Jan de Jong. Dit is dan ook de _output_ van de functie.