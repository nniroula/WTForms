from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class AddSnacksForm(FlaskForm):
    """ form for adding snacks """
    name = StringField("Snack Name")   # thing in parenthesis becomes a label for the form
    price = FloatField("Price in USD")