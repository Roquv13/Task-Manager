import exceptions

def get_task():
    try:
        name = input("Enter name of task: ")
        text = input("Enter text for task: ")
        return name, text
    except Exception as e:
        print(f"Error: {e}")
    
def add_task(tasks):
    try:
        name, text = get_task()
        if name in tasks:
            raise exceptions.ExistsException("Task already exists")
        tasks[name] = text
        print(f"Task '{name}' added.")
    except Exception as e:
        print(f"Error: {e}")

def delete_task(tasks):
    try:
        name, text = get_task()
        if name not in tasks:
            raise exceptions.ExistsException("Task does not exists.")
        tasks.pop(name)
    except Exception as e:
        print(f"Error: {e}")

def edit_task(tasks):
    name, text = get_task()
    tasks[name] = text

def print_task(tasks):
    for task, text in tasks.items():
        print(task, "-", text)