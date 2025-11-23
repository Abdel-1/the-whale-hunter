"""
main.py - Entry point for The Whale Hunter project (Day 1).

This script is used to verify that:
- The project structure is correct.
- The virtual environment's Python interpreter is being used.
"""

import sys  # Gives access to information about the Python interpreter and environment
from pathlib import Path  # Provides an object-oriented way to work with filesystem paths


def main():
    """
    Main function that prints diagnostic information about the environment.
    """

    # Path to the current file (src/main.py)
    current_file = Path(__file__)

    # Project root: go up from src/ to the project directory
    project_root = current_file.parent.parent

    print("🐋 Welcome to The Whale Hunter project!")
    print("-" * 60)

    # Show which Python executable is running this script
    print(f"Python executable in use: {sys.executable}")

    # Show the project root directory
    print(f"Project root directory: {project_root}")

    # Show the Python version (full detail)
    print(f"Python version: {sys.version}")

    print("-" * 60)
    print("If the Python path above includes 'venv', your Day 1 setup is correct.")


# This block ensures main() runs only when we execute this file directly:
#   python src/main.py
# and not when another module imports this file.
if __name__ == "__main__":
    main()
