import task_manage

while True:
    try:    
        print("Task\n1. Add task\n2. Edit task\n3. Delete task\n4. Print tasks\n5. Exit")
        user_choice = int(input("Select: "))
    except Exception as e:
        print(f"Error: {e}")

    if user_choice == 1:
        task_manage.add_task()