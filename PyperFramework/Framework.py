import sys

from Pyper import Pyper_Interface
from PyperFramework import Commands, Messages
from PyperFramework import FileManager
from PyperFramework.PipeLine import PyperPipeLine

"""

    Pyper Framework

    This package lays down the python framework for compiling
    python source files. While Pyper package contains scripts
    for compiling, this package forms the framework, in other
    words, this packages calls functions from Pyper for compiling.

    If any changes are needed in the Python Compiler Structure,
    this is the package you need to look for.

    If any changes are needed in the way python files are compiled
    to assembly, Pyper package is what you should look for.
    
    Flow Chart:
    
        User Enters a Command -> Pyper Framework Parses it ->
        
        case: File Compilations
        Let's say user enters "-f text.txt"
        
        Find text.txt -> If Exits -> send to compilation
                      -> if doesn't exist or error -> throw an error
                      
        in case of multiple files, pyper framework will first find all the
        files, and validates them, then it will send to compilatiom 
        

"""


class PyperFramework:
    """
        Pyper Framework

        Basically, PyperCanRun will be set to true on start.
        If the user wants to exit, pyper_exit() will be called.

    """

    # Constructor
    def __init__(self, run_on_intialization=False, parse_start_arguments=False):
        self._PyperCanRun = True
        # Mimicking Switch case of Java, in Java it is done by hashing. See _parse_and_run_arguments()
        self._Commands = {
            Commands.Compile_Files: self._provide_files_for_compilation,
            Commands.Compile_Directory: self._provide_directory_for_compilation,
            Commands.Help: self._help,
            Commands.Info: self._info,
            Commands.Exit: self._exit
        }

        # Check if pyper should start immediately upon object creation
        if not run_on_intialization:
            return

        # Parse start arguments
        if parse_start_arguments:
            self.parse_start_arguments(sys.argv)

        # Running Pyper
        while self.can_run():
            self.proceed()

    # Returns true it pyper can run
    def can_run(self):
        return self._PyperCanRun

    # Set's PyperCanRun to false.
    def pyper_exit(self):
        self._PyperCanRun = False

    """
        Parsing commands
        
        Commands are stored in Commands.py,
        while messages are stored in Messages.py
    
    """

    # If there are any start arguments, parse them, else print welcome message.
    def parse_start_arguments(self, argv: list):

        # Ignoring the first argument
        argv.pop(0)

        if len(argv) > 0:
            self._parse_and_run_arguments(argv)
        else:
            print(Messages.WelcomeMessage)

    # To ask for commands.
    def proceed(self):
        self._parse_and_run_arguments(input(">").strip().split(" "))

    # To Parse Arguments
    def _parse_and_run_arguments(self, argv):
        if argv[0] in self._Commands:
            self._Commands[argv.pop(0)](argv)
        else:
            print(Messages.InvalidCommandError)

    """
    
        Pyper Commands
    
    """

    # For Compiling Files
    def _provide_files_for_compilation(self, argv):

        # If no files are provided, like bruh
        if len(argv) == 0:
            print(Messages.NoFileProvidedError)

        # If there were errors in opening files, return.
        if not FileManager.validate_files(argv):
            return

        PipeLinePool = []

        # Call Pyper Interface, and provide files for compilation
        for file_path in argv:
            PipeLinePool.append(PyperPipeLine(file_path))

    # For Compiling all files inside the directory
    def _provide_directory_for_compilation(self, argv):
        print(Messages.CompiledDirectoryMessage)

    # For displaying help message
    def _help(self, argv):
        print(Messages.HelpMessage)

    # For dispalying info message
    def _info(self, argv):
        print(Messages.InfoMessage)

    # For exiting pyper
    def _exit(self, argv):
        print(Messages.GoodByeMessage)
        self.pyper_exit()
