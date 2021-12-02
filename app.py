from flask import Flask, render_template, redirect, request, flash
# from flask.templating import render_template
from forms import AddSnacksForm, NewEmployeeForm   # from module import class


app = Flask(__name__)
app.config["SECRET_KEY"] = "whatthehell"  # secret key is needed to use CSRF in the forms in wtforms, for flash messaging in flask

# To check if flask is up and running
@app.route('/')
def home_route():
    # return "<small>Flask is Fun </small>"
    return render_template("home.html")

# @app.route("/snacks/new", methods = ["GET", "POST"])
# def add_snack():
#     form = AddSnacksForm()   # form is a form object, form object comes with a field attribute, field.label
#     #raise # raise is used to get error so that you can get interactive debugger tool in browser
#     if form.validate_on_submit():  # POST method
#         return redirect('/')
#     else:  # GET method
#         return render_template("add_snack_form.html", form = form)


# @app.route("/snacks/new", methods = ["GET", "POST"])
# def add_snack():
#     print(request.form) # shows all field data, form.attribute.data gives data for that attribute(or variable)
#     form = AddSnacksForm()   # form is a form object, form object comes with a field attribute, field.label
#     #raise # raise is used to get error so that you can get interactive debugger tool in browser
#     if form.validate_on_submit():  # POST method
#         print(form.name.data)   # view this in terminal
#         print(form.price.data)
#         return redirect('/')
#     else:  # GET method
#         return render_template("add_snack_form.html", form = form)


@app.route("/snacks/new", methods = ["GET", "POST"])
def add_snack():
    form = AddSnacksForm()   # form is a form object, form object comes with a field attribute, field.label
    #raise # raise is used to get error so that you can get interactive debugger tool in browser
    if form.validate_on_submit():  # POST method
        name = form.name.data
        price = form.price.data
        
        flash(f"Created new snakc. Name is {name} and price is {price}")
        return redirect('/')  # this redirect to home page and home page(home.html) has message flashing
    else:  # GET method
        return render_template("add_snack_form.html", form = form)

"""
@app.route('/empployees/new', methods = ["GET", "POST"])
def add_employee():
    form = NewEmployeeForm()
    if form.validate_on_submit():
        name = form.name.data
        state = form.state.data
        dept_code = form.dept_code.data
        emp = Employee(name = name, state = state, dept_code = dept_code) # coz I do not have these things
        db.session.add(emp)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_employee_form.html', form = form)

"""

# Editing or updating wtforms
@app.route("/users/<int:uid>/edit", methods = ["GET", "POST"])
def edit_user(uid):
    """ Show user edit form with prepopulated html form for a user to edit """
    user = User.query.get_or_404(uid)
    depts = db.session.query(Department.dept_code, Department.dept_name)
    form = UserForm(obj = user)

    if form.validate_on_submit():
        user.name = form.name.data
        user.email. = form.email.data
        db.session.commit()
        flash(f" User {uid} updated!")
        return redirect("user_form.html", form = form)
    else:
        return render_template("user_form.html", form = form)
