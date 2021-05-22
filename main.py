from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from mongo import post_name
from flask import Flask, session, redirect, url_for, escape, request

# Creates a Flask Instance
app = Flask(__name__)
# app.config['SECRET_KEY'] = "my super secret key"
app.secret_key = 'a random string'

# Creates a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators = [DataRequired()])
    submit = SubmitField("Submit")

# Index Page
@app.route('/')
def index():
    if session.get('user') is None:
        return render_template("index.html", logged_in = False)
    return render_template("index.html", logged_in = True, user = session.get('user'))

# Logout page
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('user', None)
   return redirect(url_for('index'))

# Username page
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

# Page that shows a form
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    already_submitted = False

    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        post_name(name)
        session['user'] = name
        form.name.data = ''

    if session.get('user') is not None:
        already_submitted = True

    return render_template("name.html", name=name, form=form, 
    already_submitted = already_submitted, user = session.get('user'))

# TODO: Create a working message board

# Message page
@app.route('/messages')
def message():
    return render_template("messages.html")
