from datetime import datetime

deadline = {}

def current():
    today = datetime.today()
    today_nums = today.strftime("%d/%m/%Y")
    today_date = datetime.strptime(today_nums, "%d/%m/%Y").date()
    return today_date

def remaining_days(deadline):
    today = current()
    days_left = (deadline - today).days
    return days_left

def get_deadline(task):
    if task in deadline:
        task_deadline = deadline.get(task)
        return task_deadline
    else:
        print("This task has not setted deadline")

def deadline(task):
    if task in deadline:
        print("Task has already setted deadline")
        task_deadline = get_deadline(task)
        print(f"Deadline for this task {task_deadline}")
    else:
        while True:
            rem_date_str = input("Enter date in format day/month/year: ")
            try:
                rem_date = datetime.strptime(rem_date_str, "%d/%m/%Y").date()
                deadline[task] = rem_date
            except ValueError:
                print("Invalid date format. Please enter the date in the correct format (day/month/year)")