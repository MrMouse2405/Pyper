import os.path
from os import path

from PyperFramework import Messages

"""

    Pyper File Manager

    As the name suggests, this file is responsible for file operations.


"""
# To check if provided path is a directory
def is_directory_file(path_to_file: str) -> bool:
    return path.isdir(path_to_file)

"""
    
    Files
    
    A simple class to hold a collection of files.

"""


def _error_print(file: str, error: str):
    print(f"Pre-compilation error in path: {file}\nDetails: {error}")


# To get files.
def validate_files(paths: list[str]) -> bool:
    # iterating through all paths and validating files
    for x in paths:

        # Validation
        if not path.exists(x):  # If exists
            _error_print(x, Messages.InvalidFilePathError)
            return False

        elif not path.isfile(x) or (x[-3:] != ".py"):  # if it's not a regular file and extension doesn't ends with .py
            _error_print(x, Messages.InvalidFileTypeError)
            return False

        elif not os.access(x, os.R_OK):  # if it cannot read file
            _error_print(x, Messages.InsufficientPrivilegesError)
            return False

    # if everything is fine, return true
    return True
