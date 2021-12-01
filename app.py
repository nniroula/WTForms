from flask import Flask, render_template
# from flask.templating import render_template
from forms import AddSnacksForm   # from module import class


app = Flask(__name__)
app.config["SECRET_KEY"] = "whatthehell"  # secret key is needed to use CSRF in the forms in wtforms, for flash messaging in flask

# To check if flask is up and running
@app.route('/')
def home_route():
    return "<small>Flask is Fun </small>"

@app.route("/snacks/new", methods = ["GET", "POST"])
def add_snack():
    form = AddSnacksForm()   # form is a form object, form object comes with a field attribute, field.label
    #raise # raise is used to get error so that you can get interactive debugger tool in browser
    return render_template("add_snack_form.html", form = form)

