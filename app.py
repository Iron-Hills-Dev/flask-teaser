import logging

from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
logging.info("Activated logging")

from application import month_adapter
from application import year_adapter
