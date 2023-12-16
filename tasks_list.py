import exceptions

def create_list(lists):
    try:
        list_name = input("Enter name of list: ")
        if list_name in lists:
            raise exceptions.ExistsException("List already exists.")
        lists[list_name] = {}
        print(f"List '{list_name}' created.")
    except Exception as e:
        print(f"Error: {e}")

def select_list(lists):
    try:
        list_name = input("Enter name of list to select: ")
        if list_name not in lists:
            raise exceptions.ExistsException("List not found.")
        return list_name, lists[list_name]
    except Exception as e:
        print(f"Error: {e}")
        return None, None