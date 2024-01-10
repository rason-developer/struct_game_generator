# Pygame Project Generator

This project is a simple Python script and batch file combination that helps automate the initialization of Pygame projects by setting up a default directory structure and files.

## Contents

- [Purpose](#purpose)
- [Usage](#usage)
- [Batch File (.bat)](#batch-file-bat)
- [Python Script (.py)](#python-script-py)
- [Contributing](#contributing)
- [License](#license)

## Purpose

The purpose of this project is to streamline the setup process for Pygame projects. It includes a Python script (`pygame_generator.py`) that creates a folder structure and initializes files commonly used in my Pygame projects.

## Usage

1. **Ensure Python and pygame are Installed:** Before using the Pygame Project Generator, ensure Python and pygame are installed on your system.

2. **Clone or Download the Repository:** Clone or download this repository to your local machine.

3. **Run the Batch File:** Execute the `run_pygame_generator.bat` file by double-clicking on it. This batch file locates the Python script and runs it to generate the Pygame project structure.

4. **Follow Instructions:** The script will create the necessary folder structure and default files required for a Pygame project.

## Batch File (.bat)

The `run_pygame_generator.bat` file is a batch script that automates the execution of the Python script to generate the Pygame project structure.

### Customizing the Batch File

You may need to modify the batch file if:
- Python is not in your PATH environment variable.
- The Python script (`pygame_generator.py`) is renamed or located in a different directory.

The batch file automatically finds the Python script (`pygame_generator.py`) in the same directory as the batch file using the `%~dp0` variable.

## Python Script (.py)

The `pygame_generator.py` Python script creates the folder structure and initializes default files for the Pygame project.

### Customizing the Python Script

You can customize the default code snippets within the Python script to match your desired structure or default content for the generated files.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
