from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask.globals import request
from passlib.hash import pbkdf2_sha256 as passlib
from flask_login import login_user

from app import db
from app.models import User
from app.forms import LoginForm, SignUpForm

auth = Blueprint('auth', __name__, url_prefix='/authenticate')

@auth.route('/login/', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user:
      if passlib.verify(form.password.data, user.password):
        login_user(user)

        next = request.args.get('next')
        flash('U bent nu ingelogd!')
        return redirect(next or url_for('posts.index'))
      else:
        flash('U heeft geen correct wachtwoord opgegeven, probeer het opnieuw!')
        return redirect(url_for('auth.login'))
    else:
      flash('Deze gebruiker is niet gevonden, probeer het opnieuw')
      return redirect(url_for('auth.login'))
    
  return render_template('/auth/login.html', form=form)

@auth.route('/signup/', methods=['GET', 'POST'])
def signup():
  form = SignUpForm()
  if form.validate_on_submit():
    hash = passlib.hash(form.password.data)
    user = User(name=form.name.data, email=form.email.data, username=form.username.data, password=hash)

    db.session.add(user)
    db.session.commit()

    flash('U bent succesvol aangemeld. Log nu in.')
    return redirect(url_for('auth.login'))
  return render_template('/auth/signup.html', form=form)