from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
  email = StringField('Vul je e-mailadres in', validators=[DataRequired(message='Dit veld is verplicht!'), Email(message='Vul een geldig e-mailadres in!')])
  password = PasswordField('Vul je wachtwoord in', validators=[DataRequired(message='Dit veld is verplicht!')])
  submit = SubmitField('Log in') 

class SignUpForm(FlaskForm):
  name = StringField('Vul je naam in', validators=[DataRequired(message='Dit veld is verplicht!')])
  username = StringField('Maak een gebruikersnaam aan', validators=[DataRequired(message='Dit veld is verplicht!')])
  email = StringField('Vul je e-mailadres in', validators=[DataRequired(message='Dit veld is verplicht!'), Email(message='Vul een geldig e-mailadres in!')])
  password = PasswordField('Maak een nieuw wachtwoord aan', validators=[DataRequired(message='Dit veld is verplicht!')])
  confirm = PasswordField('Herhaal je wachtwoord', validators=[EqualTo('password', message='Dit veld moet gelijk zijn aan wachtwoord')])
  submit = SubmitField('Meld Aan') 

class EditAccountForm(FlaskForm):
  name = StringField('Wijzig je naam', validators=[DataRequired(message='Dit veld is verplicht!')])
  username = StringField('Wijzig je gebruikersnaam', validators=[DataRequired(message='Dit veld is verplicht!')])
  email = StringField('Wijzig je e-mailadres', validators=[DataRequired(message='Dit veld is verplicht!'), Email(message='Vul een geldig e-mailadres in!')])
  submit = SubmitField('Wijzig Account') 