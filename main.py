from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from mongo import post_name

# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key"

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators = [DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        post_name(name)
        form.name.data = ''

    return render_template("name.html", name=name, form=form)

