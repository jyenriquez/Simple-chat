from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")