# Module for deleting airplane models and systems from the inventory.
# Contains functions to render menus, display options, and perform delete operations.

from helpers import intake_user_choice as intake_user_choice
from helpers import intake_system as intake_system
from helpers import intake_airplane_model as intake_airplane_model
from helpers import get_dummy_data as get_dummy_data
from helpers import set_dummy_data as set_dummy_data

def render_delete_menu():
    """
    Renders the delete menu options as a formatted string.

    Returns:
        str: The formatted menu string for deleting airplane models or systems.
    """
    menu_title = "DELETE MENU"
    length = len(menu_title)
    menu = f"""
\n{'=' * length}\n{menu_title}\n{'=' * length}
1. Delete airplane model
2. Delete system
3. Back to main menu
"""
    return menu

def show_delete_menu():
    """
    Prints the delete menu to the console.
    """
    print(render_delete_menu())


def delete_model(model):
    """
    Deletes an airplane model from the dummy data.

    Args:
        model (str): The name of the airplane model to delete.

    Prompts for confirmation before deletion.
    """
    data = get_dummy_data()
    # print(data)
    del_indx = ''
    for i in range(len(data)):
        if data[i]['model'] == model:
            del_indx = i
        i += 1
    input(f"Are you sure you want to delete {model} from dummy-data?\nEnter y for yes or enter to abort: ")
    del data[del_indx]
    set_dummy_data(data)
# delete_model('f-15')
# print(get_dummy_data())


def delete_system(model, system):
    """
    Deletes a system from a specific airplane model.

    Args:
        model (str): The airplane model from which to delete the system.
        system (str): The name of the system to delete.

    Handles both main systems and peripheral systems.
    """
    data = get_dummy_data()
    is_peripheral = False
    del_indx = ''
    del_key = ''
    for i in range(len(data)):
        if data[i]['model'] == model:
            for cur_system in data[i]['systems']:
                if cur_system == 'peripheral-systems':
                    for cur_system in data[i]['systems']['peripheral-systems']:
                        if cur_system == system:
                            is_peripheral = True
                            del_indx = i
                            del_key = cur_system
                else:
                    if cur_system == system:
                        is_peripheral = False
                        del_indx = i
                        del_key = cur_system
    input(f"Are you sure you want to delete {model} {system} from dummy-data?\nEnter y for yes or enter to abort: ")
    if is_peripheral:
        del data[del_indx]['systems']['peripheral-systems'][del_key]
    else:
        del data[del_indx]['systems'][del_key]
        
    set_dummy_data(data)
# delete_system('f-15', 'air-frame')
# print(get_dummy_data())


def delete_menu():
    """
    Displays the delete menu and handles user choices for deleting models or systems.
    """
    delete_menu_on = True
    while delete_menu_on:
        
        show_delete_menu()

        delete_menu_user_choice = intake_user_choice()
    
        if delete_menu_user_choice == 1:
            # Delete airplane model
            model = intake_airplane_model()
            delete_model(model)
        
        if delete_menu_user_choice == 2: 
            # Delete system from model
            model = intake_airplane_model()
            system = intake_system()
            delete_system(model, system)

        if delete_menu_user_choice == 3:
            delete_menu_on = False
            msg = "Returning to main menu"
            print(f"\n{'-' * 30} {msg} {'-' * 30}")