# PRAC_7
# Guitar Inventory Management System

This repository contains two Python files, `guitar.py` and `myguitars.py`, which together form a simple inventory management system for guitars.

## `guitar.py`

`guitar.py` defines the `Guitar` class, which represents a single guitar object. Each `Guitar` object has attributes for its name, year of manufacture, and cost. Additionally, it provides methods for calculating the age of the guitar and determining if it is considered vintage. The class also includes methods for loading guitars from a CSV file (`load_guitars`) and saving guitars to a CSV file (`save_guitars`).

## `myguitars.py`

`myguitars.py` is the main program file that utilizes the `Guitar` class defined in `guitar.py`. This file provides functionality for managing a list of guitars, including loading existing guitars from a CSV file, displaying the list of guitars, sorting them by year, allowing the user to input new guitars, and saving the updated list to the CSV file.

## Usage

To use this inventory management system:

1. Ensure both `guitar.py` and `myguitars.py` are in the same directory.
2. Run `myguitars.py` using a Python interpreter.
3. Follow the prompts to view, add, and save guitars.

# Pythonic Project Management

This is a simple project management program written in Python. It allows users to load, save, display, filter, add, and update projects using a menu-driven interface.

## Files

- `project.py`: Defines the `Project` class.
- `project_management.py`: Main program file containing the menu and functionalities.
- `projects.txt`: Data file containing project information.

## Usage

1. Run `project_management.py` to start the program.
2. Choose from the menu options to perform various actions:
   - Load projects
   - Save projects
   - Display projects
   - Filter projects by date
   - Add new project
   - Update project
   - Quit
3. Follow the prompts to input data or select options as needed.

## Dependencies

- Python 3.x

## Contributing

Contributions are welcome! If you'd like to improve this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
