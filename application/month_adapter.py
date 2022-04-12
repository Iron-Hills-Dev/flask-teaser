from app import app
from domain.date import month_service


@app.route("/month/days-left", methods=["GET"])
def month_days_left():
    """
    :return: Amount of days left to end of the month
    """
    # TODO docs
    return {"days-left": month_service.get_days_left()}
