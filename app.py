import logging

from flask import Flask

from infrastructure.config.environ_config import import_all_envs
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

# envs
import_all_envs(app.config)

# application ports configuration
ports = AppPorts(app.config)
logging.info("Configured app ports")

from application import year_adapter
from application import month_adapter
from application.car import car_rest_adapter
