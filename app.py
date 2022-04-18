import logging

from infrastructure.config.ports_config import AppPorts
from infrastructure.logging.logging_formatter import CustomFormatter

from flask import Flask

app = Flask(__name__)

# logger handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
# logger handler

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)

logging.info("Activated logging")

# application ports configuration
ports = AppPorts()

from application import month_adapter
from application import year_adapter
from application.car import car_rest_adapter
