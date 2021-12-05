from queue import Queue
from PyperFramework.Pyper_Thread import PyperThread

"""

    Phase 2 SRC To AST
    
    This class is responsible for calling several functions from Pyper.
    
    In brief, this class does A lot, tokenizes, creates lexemes, 
    analyzes syntax on the fly and catches errors during compilation (the beauty of python),
    and then finally converts to Pyper AST.
    


"""


class Phase2SRCToAST(PyperThread):

    def __init__(self, withdrawal_queue: Queue, deposit_queue: Queue):
        super().__init__(withdrawal_queue, deposit_queue)

    """
    
        When the thread starts, 
        what should we do :?
    
    """

    def on_start(self):
        pass

    """
        
        While running, 
        what should we do ;?
    
    """

    def on_stepped(self):
        if len(self.withdrawal_queue.queue) == 0:
            if self._Last._Running:
                print(f"Thread: {self.name} is waiting")
            else:
                self.exit_pyper_thread()
        else:
            print(self.withdrawal_queue.get())

    """
    
        When exiting,
        what should we do O_O?
    
    """

    def on_exit(self):
        pass

    """
        
        When terminated,
        just perform some clean up.
    
    """

    def on_terminated(self):
        super().deposit_queue.empty()
