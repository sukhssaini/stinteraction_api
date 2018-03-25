from os.path import join, dirname
from dotenv import load_dotenv
from api import app

load_dotenv(join(dirname(__file__), ".env"))

app.run(debug=True, port=5002)
