from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask.globals import request
from passlib.hash import pbkdf2_sha256 as passlib
from flask_login import login_user, logout_user, login_required, current_user

from app import db
from app.models import User
from app.forms import LoginForm, SignUpForm, EditAccountForm

auth = Blueprint('auth', __name__)


# login route

@auth.route('/auth/login/', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    flash('U bent al ingelogd')
    return redirect(url_for('lessons.index'))
  
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user:
      if passlib.verify(form.password.data, user.password):
        login_user(user)

        next = request.args.get('next')
        flash('U bent nu ingelogd!')
        return redirect(next or url_for('lessons.index'))
      else:
        flash('U heeft geen correct wachtwoord opgegeven, probeer het opnieuw!')
        return redirect(url_for('auth.login'))
    else:
      flash('Deze gebruiker is niet gevonden, probeer het opnieuw')
      return redirect(url_for('auth.login'))
    
  return render_template('/auth/login.html', form=form)


# signup route

@auth.route('/auth/signup/', methods=['GET', 'POST'])
def signup():
  if current_user.is_authenticated:
    flash('U bent al ingelogd')
    return redirect(url_for('lessons.index'))
  
  form = SignUpForm()
  if form.validate_on_submit():
    hash = passlib.hash(form.password.data)
    user = User(name=form.name.data, email=form.email.data, username=form.username.data, password=hash)

    db.session.add(user)
    db.session.commit()

    login_user(user)

    return redirect(url_for('auth.welcome_user'))
  return render_template('/auth/signup.html', form=form)


# logout route

@auth.route('/account/settings/logout/')
@login_required
def logout():
  logout_user()
  flash('Je bent nu uitgelogd')
  return redirect(url_for('lessons.index'))


# account route

@auth.route('/account/')
def account_redirect():
  return redirect(url_for('auth.account'))

@auth.route('/account/settings/', methods=['GET', 'POST'])
def account():
  form = EditAccountForm()

  if request.method == 'GET':
    form.name.data = current_user.name
    form.email.data = current_user.email
    form.username.data = current_user.username
  elif form.validate_on_submit():
    current_user.name = form.name.data
    current_user.email = form.email.data
    current_user.username = form.username.data

    db.session.commit()
    flash('Jouw persoonlijke gegevens zijn aangepast')
    return redirect(url_for('auth.account'))

  return render_template('auth/account.html', form=form)


# welcome user route

@auth.route('/auth/signup/welcome/')
@login_required
def welcome_user():
  return render_template('auth/welcome-user.html')