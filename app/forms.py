from wtforms.fields.core import SelectField

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
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

class NewCourseForm(FlaskForm):
  title = StringField('Voeg een titel toe aan de les', validators=[DataRequired(message='Dit veld is verplicht!')])
  body = TextAreaField('Voeg content toe aan de les', validators=[DataRequired(message='Dit veld is verplicht!')])
  course = SelectField('Voeg toe aan een cursus')
  submit = SubmitField('Voeg de les toe')

class EditLessonForm(FlaskForm):
  title = StringField('Wijzig de titel van de les', validators=[DataRequired(message='Dit veld is verplicht!')])
  body = TextAreaField('Wijzig de content van de les', validators=[DataRequired(message='Dit veld is verplicht!')])
  submit = SubmitField('Wijzig de les')