from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flaskext.markdown import Markdown
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  db.init_app(app)
  migrate.init_app(app, db)
  login_manager.init_app(app)
  Markdown(app)

  from app.views.lessons import lessons
  from app.views.auth import auth
  app.register_blueprint(lessons)
  app.register_blueprint(auth)

  return app