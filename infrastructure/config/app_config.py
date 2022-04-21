import logging
from os import environ


def set_app_config(_app):
    if environ.get("CAR_PORT") is None:
        logging.critical("[set_app_config] Variable CAR_PORT not given - aborting init")
        exit(1)
    else:
        _app.config.update({"CAR_PORT": environ.get("CAR_PORT")})
        logging.debug("[set_app_config] Variable CAR_PORT has been set")
