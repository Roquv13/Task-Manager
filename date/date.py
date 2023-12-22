import datetime
from datetime import date

def current():
    today = date.today()
    today_nums = today.strftime("%d/%m/%Y")
    return today_nums

def deadline():
    while True:
        task_date_in = input("Enter date in format year/month/day")
        try:
            task_date = datetime.strftime(task_date_in, "%d/%m/%Y")
            return task_date
        except ValueError:
            print("Invalid date format. Please enter the date in the correct format (year/month/day)")

def days_to_end():
    days = deadline() -  current()
    return days