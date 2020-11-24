# Keuze opdracht Python/Flask
Python/Flask project voor keuze opdracht informatica 2020

Om het project te starten, voer de volgende commando's uit:
```bash
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ flask run
```

Om ook browser-sync te starten, voer de volgende commando's uit:
```bash
$ npm install -g browser-sync
$ browser-sync start --proxy http://127.0.0.1:5000/ --files="app/templates/**, app/static/**" --no-notify
```