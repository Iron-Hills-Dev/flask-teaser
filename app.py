import logging

from flask import Flask

from infrastructure.config.app_config import set_app_config
from infrastructure.config.ports_config import AppPorts
from infrastructure.logging.logging_formatter import CustomFormatter

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

# app config set
set_app_config(app)

# application ports configuration
ports = AppPorts(app.config["CAR_PORT"])

from application import month_adapter
from application import year_adapter
from application.car import car_rest_adapter