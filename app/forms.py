# imports for the packages and/or modules we need
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class newAnimalForm(FlaskForm):
    # name, weight, height, climate, region
    name = StringField('Name', validators=[DataRequired()])
    weight = IntegerField('Weight')
    height = IntegerField('Height')
    climate = StringField('Climate')
    region = StringField('Region')
    submit_button = SubmitField()

class newUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit_button = SubmitField()

class loginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()