
# Main application file for the inventory manager.
# This script initializes the application, loads data, and runs the main menu loop.

from render_menu import show_main_menu as show_main_menu
from display_menu import display_menu as display_menu
from update import update_manu as update_manu
from add import add_menu as add_menu
from delete import delete_menu as delete_menu

from helpers import intake_user_choice as intake_user_choice
from helpers import get_data_base as get_data_base
from helpers import set_data_base as set_data_base
from helpers import set_dummy_data as set_dummy_data
from helpers import get_dummy_data as get_dummy_data



### VARIABLES ###
is_saved = False # set to true on user save, set to false on data change
on = True

### METHODS ###

### LOGIC ###
# Initiate data in dummy-data
data_base = get_data_base()
set_dummy_data(data_base)

print("\n\nWELCOME TO INVENTORY MNGR")

# Display main menu and get user choice
while on:
    # with open()

    show_main_menu()

    user_choice = intake_user_choice()

    if user_choice == 1: # DISPLAY MENU
        # Open sub-menu for displaying save or cache data after create / read / update / delete
        display_menu()
        
    if user_choice == 2: # UPDATE
        # Update dummy data
        update_manu()

    if user_choice == 3: # ADD NEW -> 1.part, 2.airplane
        # Add new data to dummy data
        add_menu()

    if user_choice == 4:  # DELETE
        # Delete data from dummy data
        delete_menu()

    if user_choice == 5: # SAVE TO FILE
        dummy_data = get_dummy_data()
        continue_choice = input("Are you sure you want to commit data permanently?\nTHESE ACTION IS PERMANENT !\nEnter y for yes or press enter to abort")
        if continue_choice == 'y':
            set_data_base(dummy_data)

    if user_choice == 6: # EXIT
        message = "Thank you for using INVENTORY MNGR"
        print(f"\n\n{'=' * len(message)}\n{message}\n{'=' * len(message)}\n\n")
        on = False
