# Module for adding new airplane models and systems to the inventory.
# Contains functions to render menus, display options, and perform add operations.

from helpers import get_dummy_data as get_dummy_data
from helpers import set_dummy_data as set_dummy_data
from helpers import intake_airplane_model as intake_airplane_model
from helpers import intake_user_choice as intake_user_choice

def render_add_menu():
    """
    Renders the add menu options as a formatted string.

    Returns:
        str: The formatted menu string for adding new airplane models or systems.
    """
    menu_title = "ADD MENU"
    length = len(menu_title)
    menu = f"""
\n{'=' * length}\n{menu_title}\n{'=' * length}
1. Add new airplane model
2. Add new system to airplane model
3. Back to main menu
"""
    return menu

def show_add_menu():
    """
    Prints the add menu to the console.
    """
    print(render_add_menu())

def add_new_airplane_model(new_model):
    """
    Adds a new airplane model to the dummy data.

    Args:
        new_model (str): The name of the new airplane model to add.

    Prompts the user for confirmation and initializes the model with default systems.
    """
    data = get_dummy_data()
    new_data = {'model': new_model}
    data.append(new_data)
    continue_choice = input("Enter y to initialize the new model with default data or press enter to abort: ")
    if continue_choice == 'y':
        for model in data:
            # print(model)
            if model['model'] == new_model:
                model['id'] = 34567890
                model['systems'] = {}
                # print(data)
                cur_system_inventory = {}
                for system, inventory in data[0]['systems'].items():
                    cur_system_inventory.update({system: inventory})
                    model['systems'].update(cur_system_inventory)
    save_data_choice = input("The data is ready\nAre you sure you want to add it to the dummy-data?\nEnter y for yes or press enter to abort: ")
    if save_data_choice == 'y':
        set_dummy_data(data)
    print(f"New airplane {new_model} succesfully added to dummy-data")
# add_new_airplane_model('f-14')

def add_new_inventory(model, new_system):
    """
    Adds a new system to an existing airplane model.

    Args:
        model (str): The airplane model to add the system to.
        new_system (str): The name of the new system to add.

    Initializes the new system with default inventory values.
    """
    data = get_dummy_data()

    for i in range(len(data)):
        if data[i]['model'] == model:
            new_inventory = {new_system: {"available": 50, "gross": 100, "net-req": 70}}
            data[i]['systems'].update(new_inventory)
        i += 1
    save_data_choice = input("The data is ready\nAre you sure you want to add it to the dummy-data?\nEnter y for yes or press enter to abort: ")
    if save_data_choice == 'y':
        set_dummy_data(data)
    print(f"New system {new_system} added to {model} succesfully and added to dummy-data")
# add_new_inventory()



def add_menu():
    """
    Displays the add menu and handles user choices for adding models or systems.
    """
    add_menu_on = True
    while add_menu_on:
        
        show_add_menu()

        add_menu_user_choice = intake_user_choice()
    
        if add_menu_user_choice == 1:
            # Add new airplane
            new_model = input("Enter new airplane model to add ")
            add_new_airplane_model(new_model)

            continue_choice = input("Enter y to update another inventory or press enter to go back to main menu")
            if continue_choice == 'y':
                add_menu()
        
        if add_menu_user_choice == 2: 
            model = intake_airplane_model()
            new_system = input("Enter new system to add ")

            add_new_inventory(model, new_system)

            continue_choice = input("Enter y to update another inventory or press enter to go back to main menu")
            if continue_choice == 'y':
                add_menu()

        if add_menu_user_choice == 3:
            add_menu_on = False
            msg = "Returning to main menu"
            print(f"\n{'-' * 30} {msg} {'-' * 30}")
