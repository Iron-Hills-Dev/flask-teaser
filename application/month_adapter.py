import logging
from datetime import date

from flask import request

from app import app
from domain.date import month_service


@app.route("/month/days-left", methods=["GET"])
def month_days_left():
    """
    :return: Amount of days left to end of the month
    """
    logging.info("[/month/days-left] Endpoint triggered")
    try:
        if request.headers["Accept"] != "application/json":
            logging.error("[/month/days-left] Wrong 'Accept' header given.")
            return {"error": 1, "desc": "Wrong 'Accept' header"}, 406
    except KeyError:
        logging.error("[/month/days-left] No 'Accept' header given.")
        return {"error": 2, "desc": "No 'Accept' header given"}, 406
    logging.debug("[/month/days-left] 'Accept' header validated")
    return {"daysLeft": month_service.get_days_left(date.today())}, 200
