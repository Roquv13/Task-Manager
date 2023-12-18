import task_manage
import exceptions

def completed(tasks, completed_tasks):
    try:
        name = task_manage.get_name()
        text = tasks.get(name)
        if name not in tasks:
            raise exceptions.ExistsException("Task does not exists.")
        completed_tasks[name] = text
        tasks.pop(name)
        print("Task mark as completed")
    except Exception as e:
        print(f"Error: {e}")