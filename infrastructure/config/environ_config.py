import logging
from os import environ

from flask import Config

ENV_PREFIX = "TEASER_"

default_envs = {"TEASER_CAR_DATA_DIR": "/tmp/teaser_car_data"}


def import_all_envs(_config: Config):
    for k, v in environ.items():
        if k.startswith(ENV_PREFIX):
            _config.update({k: v})

    for k in default_envs:
        if _config.get(k) is None:
            logging.warning(f"Using default env variable: {k}={default_envs[k]}")
            _config.update({k: default_envs[k]})
