from queue import Queue
from PyperFramework.Pyper_Thread import PyperThread

"""
    
    Phase 1 File Reader
    
    This class is responsible for reading python source code files line by line
    and caching them.
    

"""


class Phase1FileReader(PyperThread):

    def __init__(self, deposit_queue: Queue, path_to_file_for_reading: str):
        super().__init__(None, deposit_queue)
        self.file_to_read = open(path_to_file_for_reading, mode='r')
        self.name = f"Thread: {self.file_to_read.name} Phase 1"

    """
    
        Reading the line.
        
        We are reading the file line by file instead of reading everything at once.
    
    """

    def _read_line(self):
        read_line = self.file_to_read.readline()

        if not read_line:
            self.exit_pyper_thread()

        self.deposit_queue.put(read_line)

    """
    
        When the thread starts,
        at least reading some lines so that the next thread doesn't have to wait.
    
    """

    def on_start(self):
        for x in range(5):
            self._read_line()

    """
       
        We are now inside the thread loop,
        keep on reading lines until we reach EOF
        
    """

    def on_stepped(self):
        self._read_line()

    """
        
        When the thread ends,
        do nothing?
        
    """

    def on_exit(self):
        pass

    """
    
        When the thread is terminated,
        clear everything stored in deposit queue
    
    """

    def on_terminated(self):
        self.deposit_queue.empty()
