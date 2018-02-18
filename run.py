from os.path import join, dirname
from os import environ
from dotenv import Dotenv
from api import app

environment = Dotenv(join(dirname(__file__), ".env"))
environ.update(environment)

app.run(debug=True, port=5002)
