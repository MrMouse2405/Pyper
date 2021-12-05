from PyperFramework.Framework import PyperFramework

'''
    Project Pyper

    Understanding the file structure
    
    - Pyper
      The pyper compiler.
      - Pyper.Pyper_Interface
        A file containing all the functions you might need to interact with the compiler.
        
    - Pyper Framework
      The compiler framework.
      Pyper compiler just holds files needed for compiling python source code.
      To actually run the functions stored in those files in sequence, Pyper Framework
      is used. Pyper Framework is responsible for not only calling functions,
      but also acting as an interface between user and the pyper compiler.
      - PyperFramework.Framework.PyperFramework
        this is class that encapsulates the entire pyper framework. Initialize this class to use the
        framework, or set kwarg run_on_initialization to true to let it run by itself.
        
    - Pyper Runtime Environment
    
    
'''

if __name__ == "__main__":
    Pyper_Framework = PyperFramework(run_on_intialization=True, parse_start_arguments=True)

