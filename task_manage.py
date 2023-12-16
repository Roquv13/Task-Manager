tasks = {}

def add_task():
    task_name = input("Enter name of task: ")
    task_text = input("Enter text for task: ")
    tasks[task_name] = task_text