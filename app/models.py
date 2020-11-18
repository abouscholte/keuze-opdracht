from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)
  admin = db.Column(db.Boolean, default=False)

  def __repr__(self):
    return '<User %r>' % self.username