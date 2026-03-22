# Module for rendering menu strings.
# Contains functions to generate formatted menu text for various application menus.

def generate_main_menu():
    """
    Generates the main menu as a formatted string.

    Returns:
        str: The main menu string.
    """
    menu_title = "MAIN MENU"
    length = len(menu_title)
    menu = f"""
\n{'=' * length}\n{menu_title}\n{'=' * length}
1. Display data -> 1. display cache, 2. display data base
2. Update data
3. Add new data
4. Delete data
5. Commit data
6. Exit program
"""
    return menu


def generate_display_menu():
    """
    Generates the display menu as a formatted string.

    Returns:
        str: The display menu string.
    """
    menu_title = "DISPLAY MENU"
    length = len(menu_title)
    menu = f"""
\n{'=' * length}\n{menu_title}\n{'=' * length}
1. Display by  part
2. Display by airplane
3. Back to main menu
"""
    return menu

def generate_display_by_part_menu():
    """
    Generates the display by part menu as a formatted string.

    Returns:
        str: The display by part menu string.
    """
    menu_title = "DISPLAY PART MENU"
    length = len(menu_title)
    menu = f"""
\n{'=' * length}\n{menu_title}\n{'=' * length}
1. Display part for all models
2. Display part for one model
3. Back to main display menu
"""
    return menu

def generate_display_by_model_menu():
    """
    Generates the display by model menu as a formatted string.

    Returns:
        str: The display by model menu string.
    """
    menu_title = "DISPLAY BY AIRPLANE MENU"
    length = len(menu_title)
    menu = f"""
\n{'=' * length}\n{menu_title}\n{'=' * length}
1. Display all parts by airplane
2. Display all parts for all airplanes
3. Back to main display menu
"""
    return menu


def show_main_menu():
    """Prints the main menu to the console."""
    print(generate_main_menu())

def show_display_menu():
    """Prints the display menu to the console."""
    print(generate_display_menu())

def show_display_by_part_menu():
    """Prints the display by part menu to the console."""
    print(generate_display_by_part_menu())

def show_display_by_model_menu():
    """Prints the display by model menu to the console."""
    print(generate_display_by_model_menu())
