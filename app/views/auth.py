from flask import Blueprint, render_template
from app.forms import LoginForm, SignUpForm

auth = Blueprint('auth', __name__, url_prefix='/authenticate')

@auth.route('/login/', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    return form.email.data + ' ' +  form.password.data
  return render_template('/auth/login.html', form=form)

@auth.route('/signup/', methods=['GET', 'POST'])
def signup():
  form = SignUpForm()
  if form.validate_on_submit():
    return form.email.data + ' ' +  form.password.data
  return render_template('/auth/signup.html', form=form)