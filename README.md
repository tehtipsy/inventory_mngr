# Inventory Manager

A Python-based command-line application for managing airplane system inventory. This application allows users to create, read, update, and delete inventory records for different airplane models and their associated systems.

## Overview

The Inventory Manager is designed to help manage and track inventory levels for various airplane systems across multiple aircraft models. It provides a user-friendly menu interface for performing CRUD (Create, Read, Update, Delete) operations on inventory data.

## Features

- **Display Inventory Data**: View inventory information by system or by airplane model
- **Add New Data**: Add new airplane models or systems to the inventory
- **Update Inventory**: Modify inventory values (available, gross, net-required) for specific systems
- **Delete Data**: Remove airplane models or systems from the inventory
- **Persistent Storage**: Save and load data from JSON files
- **Menu-Driven Interface**: Easy-to-navigate menu system for all operations
- **Multiple View Options**: Display inventory by system across all models or by individual models

## Project Structure

```
inventory_mngr/
├── main.py                 # Main application entry point and menu loop
├── add.py                  # Module for adding airplane models and systems
├── delete.py               # Module for deleting airplane models and systems
├── update.py               # Module for updating inventory values
├── display_menu.py         # Menu interface for displaying data
├── display_logic.py        # Logic for retrieving and displaying inventory data
├── render_menu.py          # Functions for generating menu strings
├── helpers.py              # Utility functions for data handling and user input
├── data_base.py            # Base data structure definition
├── init_data.py            # Data initialization (reference/unused)
├── dummy_data.json         # Working/cached inventory data
├── data_base.json          # Original/persistent inventory data
└── README.md               # This file
```

## Data Structure

### Airplane Model Format

Each airplane model contains:
```json
{
  "model": "f-15",
  "id": 12345678,
  "systems": {
    "system-name": {
      "available": 30,
      "gross": 100,
      "net-req": 70
    },
    "peripheral-systems": {
      "peripheral-system-name": {
        "available": 0,
        "gross": 0,
        "net-req": 0
      }
    }
  }
}
```

### Inventory Fields

- **available**: Number of units currently available
- **gross**: Total number of units
- **net-req**: Net requirement/required units

## Installation

### Requirements

- Python 3.7 or higher

### Setup

1. Clone or download the project directory
2. Navigate to the project directory:
   ```bash
   cd inventory_mngr
   ```
3. Ensure `dummy_data.json` and `data_base.json` exist in the directory (they should be included)

## Usage

### Running the Application

Execute the main application:
```bash
python main.py
```

### Main Menu Options

Upon running the application, you'll see the main menu with the following options:

1. **Display Data**: View inventory information
   - Display by part (system across all models or for a specific model)
   - Display by airplane (all parts for a specific model or all models)

2. **Update Data**: Modify inventory values for a specific system in a model

3. **Add New Data**: 
   - Add a new airplane model
   - Add a new system to an existing model

4. **Delete Data**:
   - Delete an airplane model
   - Delete a system from a model

5. **Commit Data**: Save current changes to the persistent database

6. **Exit Program**: Exit the application

### Example Workflow

1. Start the application
2. Choose "Display Data" to view current inventory
3. Choose "Add New Data" to add a new airplane model
4. Use "Update Data" to modify inventory values
5. Choose "Commit Data" to save changes permanently to `data_base.json`
6. Exit when finished

## File Descriptions

### Core Files

- **main.py**: Application entry point that initializes data and runs the main menu loop
- **helpers.py**: Contains utility functions for:
  - Loading/saving JSON data
  - Displaying menu options
  - Getting and validating user input

- **render_menu.py**: Generates formatted menu strings for different menu types

### Functional Modules

- **add.py**: Handles creation of new airplane models and systems
- **delete.py**: Manages deletion of models and systems
- **update.py**: Updates inventory values for specific systems
- **display_menu.py**: Menu interface for displaying/viewing data
- **display_logic.py**: Retrieves and formats inventory data for display

### Data Modules

- **data_base.py**: Contains the base data structure and initial airplane definitions
- **init_data.py**: Reference module for data initialization patterns (currently unused)

## Data Files

- **dummy_data.json**: Working copy of inventory data (used during the session)
- **data_base.json**: Persistent storage of inventory data (updated when user chooses to commit)

## Airplane Models Included

By default, the application includes two airplane models:
- **F-15**: Fighter aircraft
- **F-16**: Fighter aircraft

### Default Systems

Each airplane model includes systems organized into:

**Main Systems:**
- Engine
- Air-frame
- Avionics
- Flight-controls

**Peripheral Systems:**
- Landing-gear
- Fuel-system
- Hydraulic-system
- Electrical-system

## Key Features Explained

### Display Operations

- **By System**: View a specific system's inventory across all airplane models
- **By Model**: View all systems for a specific airplane model
- **All Airplanes**: View complete inventory for all models

### Data Persistence

The application maintains two data sources:
- **Dummy Data** (dummy_data.json): Working copy loaded at startup
- **Persistent Database** (data_base.json): Only updated when user explicitly chooses to commit

This allows users to experiment with changes without permanently affecting the stored data.

## Future Enhancements

Potential improvements for future versions:
- Export inventory to CSV/Excel formats
- Batch import of inventory data
- Advanced filtering and search capabilities
- Inventory alerts/warnings for low stock
- User authentication and audit logging
- Web-based interface
- Database integration (replacing JSON files)
- Reporting and analytics features

## Notes

- All data is stored in JSON format for simplicity and portability
- Changes made during a session are stored in `dummy_data.json` but won't affect `data_base.json` until explicitly committed
- The application performs confirmation prompts for destructive operations (delete, commit)

## Troubleshooting

### Issue: No data displayed
- Ensure `dummy_data.json` exists in the same directory as `main.py`
- Verify the JSON files are not corrupted

### Issue: Changes not saved
- Remember to use the "Commit Data" option to save changes permanently
- Changes are only saved to `dummy_data.json` until you commit

### Issue: Application crashes
- Ensure Python 3.7+ is installed
- Check that the JSON data files are properly formatted

## Author

Developed as part of DevOps training and inventory management system practice.

## License

This project is provided as-is for educational purposes.
