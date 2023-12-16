def get_task():
    name = input("Enter name of task: ")
    text = input("Enter text for task: ")
    return name, text

def add_task(tasks):
    name, text = get_task()
    tasks[name] = text

def delete_task(tasks):
    name, text = get_task()
    tasks.pop(name)

def edit_task(tasks):
    name, text = get_task()
    tasks[name] = text