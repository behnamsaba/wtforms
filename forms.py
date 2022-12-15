from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,BooleanField,TextAreaField,SelectField
from wtforms.validators import InputRequired,Optional, NumberRange,URL

class addPetForm(FlaskForm):
    name = StringField('Name',validators=[InputRequired()])
    species=SelectField("Type of species:",choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],validators=[InputRequired()])
    photo_url=StringField("Photo URL:",validators=[Optional(), URL()])
    age=IntegerField("Age:",validators=[Optional(), NumberRange(min=0, max=30)])
    notes=TextAreaField("Add notes:", validators=[Optional()])
    
    available=BooleanField("Is available?")

class editPetForm(FlaskForm):
    photo_url=StringField("Photo URL:",validators=[Optional(), URL()])
    age=IntegerField("Age:",validators=[Optional(), NumberRange(min=0, max=30)])
    notes=TextAreaField("Add notes:", validators=[Optional()])
    
