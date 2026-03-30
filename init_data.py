
from helpers import get_data_base as get_data_base
from helpers import get_dummy_data as get_dummy_data
from helpers import set_data_base as set_data_base
from helpers import set_dummy_data as set_dummy_data


def init_dummy_data_composer():
    inventory = []
    model = {}
    for model in get_data_base():
        cur_inventory = {}
        cur_inventory['model'] = model['model']

        for system in model['systems']:
            cur_inventory['system'] = system
            available = 0
            gross = 0
            net_req = 0
            for property, status in model['systems'][system].items():
                if property == 'available':
                    available = status
                    cur_inventory[property] = status
                if property == 'gross':
                    gross = status 
                    cur_inventory[property] = status
                if property == 'net-req':
                    net_req = gross - available
                    cur_inventory[property] = net_req
        for system in model['systems']['peripheral-systems']:
            cur_inventory['system'] = system
            for property, status in model['systems']['peripheral-systems'][system].items():
                if property == 'available':
                    available = status
                    cur_inventory[property] = status
                if property == 'gross':
                    gross = status 
                    cur_inventory[property] = status
                if property == 'net-req':
                    net_req = gross - available
                    cur_inventory[property] = net_req
        inventory.append(cur_inventory)

    return inventory

# def init_dummy_data():
#     set_dummy_data(init_dummy_data_composer())

# init_dummy_data()
# print(get_dummy_data())