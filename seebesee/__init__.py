from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/alexa')

from . import intents
