from datetime import date

def current():
    today = date.today()
    today_nums = today.strftime("%d/%m/%Y")
    return today_nums

def deadline():
    rem_date = input("Enter date in format year/month/day")
    return rem_date

def days_to_end():
    days = deadline() -  current()
    return days