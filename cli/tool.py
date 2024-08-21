#
# Consume python file and send to cython
#


# imports
import argparse
import os.path
import pathlib


# parser
parser = argparse.ArgumentParser(description='Read in python file and send to cython')
parser.add_argument('filenames', metavar='F', type=str, nargs='+', help='filenames to convert from python to c')


# current directory
WORKING_DIR = pathlib.Path().resolve()


#
# Working python extension
#
def check_extension(f):
    if not f.endswith('.py'):
        f += ".py"
    return f


#
# Working read file
#
def file_read(f):
    clean_file_path = os.path.normpath(f)
    file_contents = open(clean_file_path, "r")
    contents = file_contents.read()
    file_contents.close()
    return contents


#
# Main cli login
#
def cli():
    args = parser.parse_args()
    all_files = args.filenames
    for file in all_files:
        try :
            file_py = check_extension(file)
            file_path = os.path.join(WORKING_DIR, file_py)
            print("")
            print("Processing file : " + file_path)
            print("")
            print(file_read(file_path))
        except:
            print("Not processing file " + file)


if __name__ == '__main__':
    cli()
