from datetime import date

def current():
    today = date.today()
    return today

def deadline():
    rem_date = input("Enter date in format year.month.day")
    return rem_date

def days_to_end():
    days = deadline() -  current()
    return days