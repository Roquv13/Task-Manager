import list_manage
import task
import exceptions

def interface(lists):
    while True:
        print("\nUser Menu\n1. Create a new list\n2. Select list\n3. Delete list\n4. Names of lists\n5. Exit")
        try:
            choice_int = int(input("Enter number: "))
            if choice_int < 1 or choice_int > 5:
                raise exceptions.BadValue("Number must be in range 1 to 5.")
        except Exception as e:
            print(f"Error: {e}")

        if choice_int == 1:
            list_manage.create_list(lists)
        elif choice_int == 2:
            list_manage.get_lists(lists)
            name_list, selected_list = list_manage.select_list(lists)
            task.interface(name_list, selected_list)
        elif choice_int == 3:
            list_manage.delete_list(lists)
        elif choice_int == 4:
            list_manage.get_lists(lists)
        elif choice_int == 5:
            break