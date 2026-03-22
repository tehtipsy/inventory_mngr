# Module containing utility functions for data handling and user interface.
# Includes functions for loading/saving data, displaying options, and getting user input.

import json


DUMMY_DATA_PATH = "./dummy_data.json"
DATA_BASE_PATH = "./data_base.json"



# Data helpers
def get_dummy_data():
    """
    Loads and returns the dummy data from the JSON file.

    Returns:
        list: The dummy data list.
    """
    with open(DUMMY_DATA_PATH, 'r') as dummy_data_file:
        dummy_data = json.load(dummy_data_file)
    return dummy_data
# get_dummy_data()

def get_data_base():
    """
    Loads and returns the data base from the JSON file.

    Returns:
        dict: The data base dictionary.
    """
    with open(DATA_BASE_PATH, 'r') as data_base_file:
        data_base = json.load(data_base_file)
    return data_base
# get_data_base()

def set_dummy_data(data):
    """
    Saves the provided data to the dummy data JSON file.

    Args:
        data: The data to save.
    """
    with open(DUMMY_DATA_PATH, 'w') as dummy_data_file:
        json.dump(data, dummy_data_file)

def set_data_base(data):
    """
    Saves the provided data to the data base JSON file.

    Args:
        data: The data to save.
    """
    with open(DATA_BASE_PATH, 'w') as data_base_file:
        json.dump(data, data_base_file)


def get_systems_keys(user_input=''):
    """
    Retrieves the list of system keys based on user input.

    Args:
        user_input (str): 'peri' for peripheral systems, 'sys' for main systems, '' for all.

    Returns:
        list: The list of system keys.
    """

    data = get_dummy_data()
    cur_data = None
    all_keys_list = []
    cur_data_indx = 0
    periphral_systems_keys = []
    systems_keys = []

    # Determine the model with highest number of systems
    for i in range(len(data)):
        cur_systems_length = len(data[i-1]['systems']) + len(data[i-1]['systems']['peripheral-systems'])
        next_systems_length = len(data[i]['systems']) + len(data[i]['systems']['peripheral-systems'])
        if cur_systems_length > next_systems_length:
            cur_data_indx = i - 1
        if cur_systems_length < next_systems_length:
            cur_data_indx = i
        if cur_systems_length == next_systems_length:
            continue
        i += 1
    cur_data = data[cur_data_indx]

    # Get all systema keys for relevant model
    for key in cur_data['systems']:
        if key == 'peripheral-systems':
            periphral_systems_keys_list = cur_data['systems'][key].keys()
            for key in periphral_systems_keys_list:
                all_keys_list.append(key)
                periphral_systems_keys.append(key)
        else:
            all_keys_list.append(key)
            systems_keys.append(key)
    # Return systems devision by user choice
    if user_input == 'peri':
        return periphral_systems_keys
    elif user_input == 'sys':
        return systems_keys
    else:
        return all_keys_list
# print(get_systems_keys())



# Menu interface helpers
def show_model_options():
    """
    Prints the list of available airplane models.
    """
    data = get_dummy_data()
    message = f"""
"""     
    i = 0
    for i in range(len(data)):
        cur_model = data[i]['model']
        message += f"{i+1}.{cur_model}\n"
        i += 1

    print(message)
# show_model_options()

def show_system_options():
    """
    Prints the list of available systems.
    """
    message = """
"""
    i = 1
    for key in get_systems_keys():
        message += f"{i}.{key}\n"
        i += 1
    print(message)
# show_system_options()


def show_inventory_options():
    """
    Prints the inventory property options.
    """
    message = "1.available 2.gross 3.net-req"
    print(message)
# show_inventory_options()


# Input helpers
def intake_user_choice():
    """
    Prompts the user to enter a choice and returns it as an integer.

    Returns:
        int: The user's choice.
    """
    try:
        choice = int(input("Enter choice then press enter: "))
        return choice
    except ValueError as e:
        print("Invalid choice! Please enter a numeric value.")
        print(e)


def intake_airplane_model():
    """
    Displays model options and prompts the user to select an airplane model.

    Returns:
        str: The selected airplane model.
    """
    show_model_options()
    choice = input("Enter airplane model in <f-XX> format: ")
    return choice

def intake_system():
    """
    Displays system options and prompts the user to select a system.

    Returns:
        str: The selected system.
    """
    show_system_options()
    choice = str(input("Enter system name then press enter: "))
    return choice
        
def intake_property():
    """
    Displays inventory property options and prompts the user to select one.

    Returns:
        str: The selected property.
    """
    show_inventory_options()
    choice = str(input("Enter inventory property then press enter: "))
    return choice
