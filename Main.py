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
      but also acts a interface between user and the pyper compiler.
      - from PyperFramework.Framework import PyperFramework
        class that encapsulates the entire pyper framework. Initialize this class to use the
        framework, or set kwarg run_on_initialization to true to let it run by itself.

    -

    FAQs:
    
    
    - I want to make changes for syntax of Python language/Request features to python: Python Software Foundation
    - I want to update commands handler / add commands: Pyper Framework
    - I want to improve Pyper Compilers IO operations including File Manager : Pyper Framework
    - I want to change the pipelining pattern: Pyper Framework
    - I want to update console messages: Pyper Framework
    - I want to update phases / sequence of compilation: Pyper Framework
    - I want to update how pyper parses source code: Pyper
    - I want to update how pyper creates AST: Pyper
    - I want to optimize how pyper compiler compiles: Pyper
    - I want to fix bug related source code translation: Pyper
    - I want to add support for more platforms: Pyper
    - I want to update how LLVM IR is generated: Pyper
    - I want to update how memory is allocated in runtime: Pyper Runtime Environment
    - I want to update/fix/optimize garbage collection: Pyper Runtime Environment
    
    
'''

if __name__ == "__main__":
    Pyper_Framework = PyperFramework(run_on_intialization=True, parse_start_arguments=True)
