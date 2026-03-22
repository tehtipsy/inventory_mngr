# Module containing logic for displaying inventory data.
# Includes functions to retrieve and display system inventories by various criteria.

from helpers import get_dummy_data as get_dummy_data
from helpers import get_systems_keys as get_systems_keys


def get_system_inventory_all(system):
    """
    Retrieves inventory data for a specific system across all airplane models.

    Args:
        system (str): The name of the system to query.

    Returns:
        list: A list of dictionaries containing model, system, and inventory data.
    """
    inventory = []
    for model in get_dummy_data():
        cur_inventory = {}
        cur_inventory['model'] = model['model']
        if system in model['systems']:
            cur_inventory['system'] = system
            for property, status in model['systems'][system].items():
                cur_inventory[property] = status
        if system in model['systems']['peripheral-systems']:
            cur_inventory['system'] = system
            for property, status in model['systems']['peripheral-systems'][system].items():
                cur_inventory[property] = status
                
        inventory.append(cur_inventory)
    return inventory
# get_system_inventory_all('engine')
# get_system_inventory_all('landing-gear')


def display_system_inventory_all(system):
    """
    Displays inventory data for a specific system across all models.

    Args:
        system (str): The name of the system to display.
    """
    inventory = get_system_inventory_all(system)
    for model in inventory:
        message = ""
        title = f"Inventory status for {model['model']} {model['system']}"
        print(f"\n\n{'=' * len(title)}\n{title}\n{'=' * len(title)}")
        message += f"""
AVAILABLE: {model['available']}
GROSS: {model['gross']}
NET-REQ: {model['net-req']}"""     
        print(message)
    print('\n'+'-' * 45)
# display_system_inventory_all('engine')
# display_system_inventory_all('landing-gear')


def get_system_inventory_by_model(model, system):
    """
    Retrieves inventory data for a specific system in a specific model.

    Args:
        model (str): The airplane model.
        system (str): The system name.

    Returns:
        dict: A dictionary with model, system, and inventory properties.
    """
    inventory = {}
    for cur_model in get_dummy_data():
        if cur_model['model'] == model:
            inventory['model'] = cur_model['model']
            if system in cur_model['systems']:
                inventory['system'] = system
                for property, status in cur_model['systems'][system].items():
                    inventory[property] = status
            if system in cur_model['systems']['peripheral-systems']:
                inventory['system'] = system
                for property, status in cur_model['systems']['peripheral-systems'][system].items():
                    inventory[property] = status
    return inventory
# get_system_inventory_by_model('f-15', 'landing-gear')
# get_system_inventory_by_model('f-15', 'air-frame')


def display_system_inventory_by_model(model, system):
    """
    Displays inventory data for a specific system in a specific model.

    Args:
        model (str): The airplane model.
        system (str): The system name.
    """
    inventory = get_system_inventory_by_model(model, system)
    message = ""
    title = f"Inventory status for {inventory['model']} {inventory['system']}"
    print(f"\n\n{'=' * len(title)}\n{title}\n{'=' * len(title)}")
    message += f"""
AVAILABLE: {inventory['available']}
GROSS: {inventory['gross']}
NET-REQ: {inventory['net-req']}"""     
    print(message)
    print('\n'+'-' * 45)
# display_system_inventory_by_model('f-15', 'engine')
# display_system_inventory_by_model('f-15', 'landing-gear')


def display_by_model(model):
    """
    Displays the systems list for a specific airplane model.

    Args:
        model (str): The airplane model.

    Returns:
        str: The formatted message string.
    """
    parts_msg = f"""
Airplane {model}:

{'=' * len("Main parts list:")}
Systems list:
{'=' * len("Main parts list:")}
"""
    for system in get_systems_keys():
        parts_msg += f"\t- {system}\n"

    print(parts_msg)
    return parts_msg


def get_all_systems_inventory_by_model(model):
    """
    Retrieves all systems inventory data for a specific model.

    Args:
        model (str): The airplane model.

    Returns:
        dict: A dictionary with model and all systems' inventory data.
    """
    inventory = {}
    data = get_dummy_data()
    for cur_model in data:
        if cur_model['model'] == model:
            inventory['model'] = cur_model['model']
            # print(cur_model)
            for system, cur_inventory in cur_model['systems'].items():
                if system == 'peripheral-systems':
                    for peripheral_system, peripheral_inventory in cur_model['systems']['peripheral-systems'].items():
                        inventory[peripheral_system] = {}
                        for property, status in peripheral_inventory.items():
                            inventory[peripheral_system][property] = status
                else:                        
                    inventory[system] = {}
                    for property, status in cur_inventory.items():
                        inventory[system][property] = status
    return inventory
# get_all_systems_inventory_by_model('f-15')
                    
            
def display_all_systems_inventory_by_model(model):
    """
    Displays all systems inventory for a specific model in a table format.

    Args:
        model (str): The airplane model.
    """
    data = get_all_systems_inventory_by_model(model)
    message = """
"""
    for property, info in data.items():
        if property == 'model':
            message += f"\nModel: {info}"
            table_head = f"{"SYSTEM":20}|{"AVAILABLE":10}|{"GROSS":10}|{"NET-REQ":10}"
            message += f"\n\n{table_head}"
            message += f"\n{'-' * len(table_head)}"
        else:
            message += f"\n{property:20}|{info['available']:10}|{info['gross']:10}|{info['net-req']:10}"
    print(message)
    print('\n'+'-' * 45)
# display_all_systems_inventory_by_model('f-16')


def display_all_systems_inventory_for_all_airplanes():
    """
    Displays all systems inventory for all airplane models.
    """
    data = get_dummy_data()
    for i in range(len(data)):
        model = data[i]['model']
        display_all_systems_inventory_by_model(model)
        i += 1
    print('\n'+'-' * 45)
# display_all_systems_inventory_for_all_airplanes()



