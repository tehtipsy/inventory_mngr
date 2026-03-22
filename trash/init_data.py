# Module for initializing airplane data structures.
# Defines constants and functions to set up initial data (currently unused in the application).

# import data_base as db

airplane_names = ['f-15', 'f-16']
airplane_fields = ['id', 'systems-list', 'systems'] 
systems_list = ['engine', 'air-frame', 'avionics', 'flight-controls', 'peripheral-systems']
peripheral_systems_list = ['landing-gear', 'fuel-system', 'hydraulic-system', 'electrical-system']


staging_data = {}
dict(staging_data)


def add_airplanes():
    """Adds airplane data to the staging data dictionary.

    Returns:
        dict: The staging data with airplane information.
    """
    for airplane in airplane_names:
        staging_data[airplane] = {}
        
        for field in airplane_fields:
            id = 100
            if field == 'id':
                staging_data[airplane]['id'] = id
                id += 1
            elif field == 'systems-list':
                staging_data[airplane]['systems-list'] = systems_list
            else:
                staging_data[airplane][field] = {}

        for system in systems_list:
            staging_data[airplane]['systems'][system] = {'availabe': 0, 'gross': 0, 'net-req': 0}

            if system == 'peripheral-systems':

                staging_data[airplane]['systems'][system] = {}

                for peripheral_system in peripheral_systems_list:
                    staging_data[airplane]['systems']['peripheral-systems'][peripheral_system] = {'availabe': 0, 'gross': 0, 'net-req': 0}

        
        print(f"{'-' * 30} {airplane} {'-' * 30}")
        print(f"\n{staging_data[airplane]}\n\n")

    return staging_data 

# add_airplanes()

    
print(f"\n\n{'*' * 60}\n")
print(staging_data)
