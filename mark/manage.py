completed_list = {}
not_completed_list = {}
in_progress_list = {}
important_list = {}

marks = [completed_list, not_completed_list, in_progress_list, important_list]

def get(name_task):
    if name_task in completed_list:
        return "completed"
    elif name_task in not_completed_list:
        return "not completed"
    elif name_task in in_progress_list:
        return "in progress"
    elif name_task in important_list:
        return "important"
    else:
        return "not marked"

def move(old_name, new_name, tasks):
    selected_task = tasks[old_name]
    if old_name in completed_list:
        completed(new_name, selected_task)
    elif old_name in not_completed_list:
        not_completed(new_name, selected_task)
    elif old_name in in_progress_list:
        in_progress(new_name, selected_task)
    elif old_name in important_list:
        important(new_name, selected_task)
    else:
        print("Not marked")

def delete(name_task, mark_list):
    if name_task in mark_list:
        mark_list.pop(name_task)
        print("MARK REMOVED")

def completed(name_task, selected_task):
    try:
        for mark in marks:
            delete(name_task, mark)
        completed_list[name_task] = selected_task
        print("Task marked as 'completed'")
        print(completed_list)
    except Exception as e:
        print(f"Error: {e}")

def not_completed(name_task, selected_task):
    try:
        for mark in marks:
            delete(name_task, mark)
        not_completed_list[name_task] = selected_task
        print("Task marked as 'not completed'")
        print(not_completed_list)
    except Exception as e:
        print(f"Error: {e}")

def in_progress(name_task, selected_task):
    try:
        for mark in marks:
            delete(name_task, mark)
        in_progress_list[name_task] = selected_task
        print("Task marked as 'in progress'")
        print(in_progress_list)
    except Exception as e:
        print(f"Error: {e}")

def important(name_task, selected_task):
    try:
        for mark in marks:
            delete(name_task, mark)
        important_list[name_task] = selected_task
        print("Task marked as important")
        print(important_list)
    except Exception as e:
        print(f"Error: {e}")