completed_list = {}
not_completed_list = {}
in_progress_list = {}
important_list = {}

def completed(name_task, selected_task):
    try:
        completed_list[name_task] = selected_task
        print("Task marked as 'completed'")
        print(completed_list)
    except Exception as e:
        print(f"Error: {e}")

def not_completed(name_task, selected_task):
    try:
        not_completed_list[name_task] = selected_task
        print("Task marked as 'not completed'")
        print(not_completed_list)
    except Exception as e:
        print(f"Error: {e}")

def in_progress(name_task, selected_task):
    try:
        in_progress_list[name_task] = selected_task
        print("Task marked as 'in progress'")
        print(in_progress_list)
    except Exception as e:
        print(f"Error: {e}")

def important(name_task, selected_task):
    try:
        important_list[name_task] = selected_task
        print("Task marked as important")
        print(important_list)
    except Exception as e:
        print(f"Error: {e}")