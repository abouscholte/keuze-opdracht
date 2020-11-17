from flask import Flask
from app.config import Config

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  from app.views.posts import posts
  from app.views.auth import auth
  app.register_blueprint(posts)
  app.register_blueprint(auth)

  return app