""" 
Створіть функцію get_days_from_today(date), 
яка розраховує кількість днів між заданою датою і поточною датою. 
"""

from datetime import datetime, timedelta

def get_days_from_today(date) -> str:
    try:
        obj_datetime = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        days_diff = today.toordinal()-obj_datetime.toordinal()
        return days_diff
    except ValueError:
        print("Incorrect date format, please input in format YYYY-mm-dd")
    

