from app import app
from domain.date import month_service

@app.route("/month/days-left")
def month_days_left():
    return {"daysLeft": month_service.get_days_left()}