from flask import Flask

app = Flask(__name__)

from application import month_adapter
from application import year_adapter