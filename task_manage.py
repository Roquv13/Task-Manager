tasks = {}

def get_task():
    name = input("Enter name of task: ")
    text = input("Enter text for task: ")
    return name, text

def add_task():
    name, text = get_task()
    tasks[name] = text

def delete_task():
    name, text = get_task()
    tasks.pop(name)