from datetime import date

from flask import request

from app import app
from domain.date import month_service


@app.route("/month/days-left", methods=["GET"])
def month_days_left():
    """
    :return: Amount of days left to end of the month
    """
    try:
        if request.headers["Accept"] != "application/json":
            return {"error": 1, "desc": "Wrong 'Accept' header"}, 406
    except KeyError:
        return {"error": 2, "desc": "No 'Accept' header given"}, 406

    return {"daysLeft": month_service.get_days_left(date.today())}, 200
