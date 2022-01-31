"""
    Pyper Messages

    The following module consists of messages that will eventually
    be displayed on the terminal when the user is interacting with
    the program.

    Many different modules use this class to access these messages
    and display them on the terminal
"""

'''
    
    Welcome / Good Bye Messages

'''

WelcomeMessage = "Welcome to Pyper [Alpha]! Type -help for help."
GoodByeMessage = "Good bye!"

'''

    Help Message

'''

HelpMessage = """
Please Enter:
-d [pathToDirectory]  : To compile all Python file(s) in the provided directory.
-f [path to files...] : To compile all provided Python file(s).
-info                 : To know more about this project / Contact Devs.
-help                 : To open this menu.
-exit                 : To exit.
"""

'''

    Info Message

'''

InfoMessage = """
Pyper (Python For Performance) [Note: this is still in development]
Creator: Abdul Mannan Syed
Email  : mrmouse2405@gmail.com
Info   :
    This project was created to convert Python code to direct executable file.
    My goal is to optimize python code to be make it possible to create desktop / mobile / general application,
    without any major additions to the syntax of the language.
    Feel free to help us out on this project,
    and feel free to contact me via email provided above to contribute, or if you have any questions.""";

'''

    General Messages

'''

CompilingFilesMessage = "Compiling Files..."
CompiledFilesMessage = "Compiled Files. Lets goooo!"

CompilingDirectoryMessage = "Feature in development..."
CompiledDirectoryMessage = "Feature in development..."

'''

    Error Messages

'''

InvalidCommandError = "Invalid Command. Sad :("

InvalidFileTypeError = "Invalid File Type. Only Python Source Code Files are accepted. Unacceptable >:("
InvalidFilePathError = "Invalid Path to File. :/"
NoFileProvidedError  = "No Files are provided for compilation. BAD!"

InsufficientPrivilegesError = "Pyper doesn't have enough privileges to access the provided files. Want to get me in trouble huh?"

