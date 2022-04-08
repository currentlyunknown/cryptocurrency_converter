import os
from os.path import join, dirname

from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)

CONVERT_PRECISION = 2
EXCHANGE_RATE_PRECISION = 4
CRYPTO_URL = 'https://api.coingecko.com/api/v3/coins/markets?'
