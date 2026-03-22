
# Module for updating inventory data.
# Contains functions to modify system inventory values for specific models.

from helpers import intake_user_choice as intake_user_choice
from helpers import intake_airplane_model as intake_airplane_model
from helpers import intake_system as intake_system
from helpers import intake_property as intake_property
from helpers import show_inventory_options as show_inventory_options
from helpers import show_system_options as show_system_options
from helpers import get_dummy_data as get_dummy_data
from helpers import set_dummy_data as set_dummy_data



def render_update_menu():
    """
    Prints the update menu options.
    """
    message = """
1. Update inventory by model
2. Update inventory by system
3. Back to main menu
"""
    print(message)

def update_inventory(model, system, property):
    """
    Updates the inventory for a specific model, system, and property.

    Args:
        model (str): The airplane model.
        system (str): The system name.
        property (str): The inventory property to update.
    """
    data = get_dummy_data()

    for i in range(len(data)):
        if model in data[i]['model']:
            cur_status = 0
            if system in data[i]['systems']['peripheral-systems']:
                cur_status = data[i]['systems']['peripheral-systems'][system][property]
            else:
                cur_status = data[i]['systems'][system][property]

            print(f"UPDATE {model} {system} {property}\nCURRENT: {cur_status}")

            new_status = int(input("Enter the new amount\n"))

            print(f"UPDATING: {model} {system} {property}\nFROM {cur_status} TO {new_status}")
            input("Press enter to approve")

            if system in data[i]['systems']['peripheral-systems']:
                data[i]['systems']['peripheral-systems'][system][property] = new_status
                print(data[i])
            else:
                data[i]['systems'][system][property] = new_status
                print(data[i])
    set_dummy_data(data)
# update_inventory('f-15', 'fuel-system', 'gross')
# update_inventory('f-15', 'engine', 'gross')




def update_manu():
    """
    Displays the update menu and handles user choices for updating inventory.
    """
    render_update_menu()

    user_model_choice = intake_airplane_model()
    user_system_choice = intake_system()
    user_inventory_property_choice = intake_property()

    update_inventory(user_model_choice, user_system_choice, user_inventory_property_choice)

    continue_choice = input("Enter y to update another inventory or press enter to go back to main menu")
    if continue_choice == 'y':
        update_manu()