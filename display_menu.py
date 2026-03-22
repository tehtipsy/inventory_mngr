# Module for handling the display menu interface.
# Manages user choices for displaying inventory data by system or by model.

from render_menu import show_display_menu as show_display_menu
from render_menu import show_display_by_part_menu as show_display_by_part_menu
from render_menu import show_display_by_model_menu as show_display_by_model_menu

from display_logic import display_system_inventory_all as display_system_inventory_all
from display_logic import display_system_inventory_by_model as display_system_inventory_by_model
from display_logic import display_all_systems_inventory_by_model as display_all_systems_inventory_by_model
from display_logic import display_all_systems_inventory_for_all_airplanes as display_all_systems_inventory_for_all_airplanes

from helpers import intake_airplane_model as intake_airplane_model
from helpers import intake_system as intake_system
from helpers import intake_user_choice as intake_user_choice


def display_menu():
    """
    Displays the main display menu and handles user choices for viewing inventory data.
    """
    display_manu_on = True

    while display_manu_on:

        show_display_menu()

        display_menu_user_choice = intake_user_choice()

        if display_menu_user_choice == 1: # DISPLAY BY SYSTEM

            by_part_menu_on = True
            while by_part_menu_on:

                show_display_by_part_menu()

                by_system_user_choice = intake_user_choice()

                if by_system_user_choice == 1: #  DISPLAY SYSTEM FOR ALL MODELS
                    system_user_choice = intake_system()
                    display_system_inventory_all(system_user_choice)

                if by_system_user_choice == 2: # DISPLAY SYSTEM BY AIRPLANE
                    model = intake_airplane_model()
                    system = intake_system()
                    display_system_inventory_by_model(model, system)

                if by_system_user_choice == 3:
                    by_part_menu_on = False
                    msg = "Returning to display menu"
                    print(f"\n{'-' * 30} {msg} {'-' * 30}")

        if display_menu_user_choice == 2: # DISPLAY BY MODEL
            by_model_menu_on = True

            while by_model_menu_on:

                show_display_by_model_menu()

                by_model_user_choice = intake_user_choice()

                if by_model_user_choice == 1:
                    # Display inventory by airplane
                    model_choice = intake_airplane_model()
                    display_all_systems_inventory_by_model(model_choice)

                if by_model_user_choice == 2:
                    # Get inventory status for all airplanes
                    display_all_systems_inventory_for_all_airplanes()

                if by_model_user_choice == 3:
                    by_model_menu_on = False
                    msg = "Returning to display menu"
                    print(f"\n{'-' * 30} {msg} {'-' * 30}")

        if display_menu_user_choice == 3: # DISPLAY EXIT
            display_manu_on = False
            msg = "Returning to main menu"
            print(f"\n{'-' * 30} {msg} {'-' * 30}")
