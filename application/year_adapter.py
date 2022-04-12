from app import app
from domain.date import year_service


@app.route("/year/days-left")
def year_days_left():
    return {"daysLeft": year_service.get_days_left()}
