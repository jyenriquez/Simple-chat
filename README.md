## Local-Development

You should have [Python 3](https://www.python.org/download/releases/3.0/) and [venv](https://docs.python.org/3/library/venv.html) installed.

How to install local environment:
- run `python3 -m venv virt` to create a virtual environment
- activate venv by running `source virt/Scripts/activate`
- to start the flask app:
- `export FLASK_APP=main.py`
- `export FLASK_ENV=development`
- `flask run`

## Heroku CLI commands
- `heroku create` to create a heroku app
- `heroku rename` to change name
- `heroku logs --tail`

## Simple-chat
A simple chat web app, currently in progress