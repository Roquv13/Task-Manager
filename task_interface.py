import task_manage

while True:
    try:    
        print("Task\n1. Add task\n2. Edit task\n3. Delete task\n4. Print tasks\n5. Exit")
        user_choice = int(input("Select: "))
    except Exception as e:
        print(f"Error: {e}")

    if user_choice == 1:
        task_manage.add_task()
    elif user_choice == 2:
        task_manage.edit_task()
    elif user_choice == 3:
        task_manage.delete_task()
    elif user_choice == 4:
        task_manage.print_task()
    elif user_choice == 5:
        break