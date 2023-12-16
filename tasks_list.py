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