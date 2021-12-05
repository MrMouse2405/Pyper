import os.path
from os import path

from PyperFramework import Messages

"""

    Pyper File Manager

    As the name suggests, this file is responsible for file operations.


"""


# To check if provided path actually exists
def path_exists(path_to_file: str) -> bool:
    return path.exists(path_to_file)


# To check if provided path is a file
def is_regular_file(path_to_file: str) -> bool:
    return path.isfile(path_to_file)


# To check if provided path is a directory
def is_directory_file(path_to_file: str) -> bool:
    return path.isdir(path_to_file)


# To check if we have access to read the file
def can_read_file(path_to_file: str) -> bool:
    return os.access(path_to_file, os.R_OK)


"""
    
    Files
    
    A simple class to hold a collection of files.

"""


def _error_print(file: str, error: str):
    print(f"Error in path:{file}\n Error:{error}")


# To get files.
def validate_files(paths: list) -> bool:
    # iterating through all paths and validating files
    for x in paths:

        # Validation
        if not path_exists(x):  # If exists
            _error_print(x, Messages.InvalidFilePathError)
            return False
        elif not is_regular_file(x) or x[
                                       -3:] != ".py":  # if it's not a regular file and extension doesn't ends with .py
            _error_print(x, Messages.InvalidFileTypeError)
            return False
        elif not can_read_file(x):  # if it cannot read file
            _error_print(x, Messages.InsufficientPrivilegesError)
            return False

    # if everything is fine, return true
    return True
