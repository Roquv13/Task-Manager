import list.manage as manage
import task.interface as interface
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
            manage.create(lists)
        elif choice_int == 2:
            manage.get_lists(lists)
            name_list, selected_list = manage.select(lists)
            interface.interface(name_list, selected_list)
        elif choice_int == 3:
            manage.delete(lists)
        elif choice_int == 4:
            manage.get_lists(lists)
        elif choice_int == 5:
            break