from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
  email = StringField('Email address', validators=[DataRequired(), Email()])
  submit = SubmitField('Log in')