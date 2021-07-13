# imports for the packages and/or modules we need
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class newAnimalForm(FlaskForm):
    # name, weight, height, climate, region
    name = StringField('Name', validators=[DataRequired()])
    weight = IntegerField('Weight')
    height = IntegerField('Height')
    climate = StringField('Climate')
    region = StringField('Region')
    submit_button = SubmitField()