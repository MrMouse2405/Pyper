import asyncio
from abc import abstractmethod
from queue import Queue
from threading import Thread

# using alias 'Override' just to give me some feel :)
"""
    
    Pyper Thread
    
    This abstract class lays the blueprint of a standard pyper thread. 
    Each Pyper Phase class inherits this class as they are technically pyper threads. 
    To boost performance, Pyper doesn't read, then compile, and then convert, step by step. 
    It reads, compiles, and converts simultaneously via design pattern of Pipelining (Multithreading pattern). 
    This is where Pyper Thread becomes useful, it lays the structure to use this pattern of pipelining. 
    

"""


class PyperThread(Thread):
    """
        PyperThread

        In our pipelining pattern, each thread
        holds reference to the Node(thread) that
        comes before and after it.

        Next and Last hold references to the
        Nodes that come before and after a this node respectively.

        Starting and ending Node have their
        LastNode and NextNode as None respectively.

        This is a simple diagram showing how nodes are connected

        S: Start Node
        M: Middle Node
        E: End Node

        S <---> M <---> M <---> E

        Documentation:

        Next
        - Holds reference to the thread after it

        Last
        - Holds reference to the thread before it

        __rshift__(other)
        - Sets provided Node as this nodes Next Node

        __lshift__(other)
        - Sets provided Node as this nodes Last Node

        A side note: deposit_queue is a temp storage
        used for sharing storage between threads

    """

    def __init__(self, withdrawal_queue: Queue, deposit_queue: Queue):
        super().__init__()
        self.withdrawal_queue = withdrawal_queue
        self.deposit_queue = deposit_queue
        self._Next: PyperThread = None
        self._Last: PyperThread = None
        self._Running = True

    def connect_next(self, other):
        self._Next = other

    def connect_last(self, other):
        self._Last = other

    """
    
        How pyper thread works.
        
        I am sure you have an idea of
        how pipelining is implemented.
        
        Now its time to discuss how
        threads run during run time.
        
        Since this class extends java.lang.Thread
        for multithreading. It overrides method run()
        to perform whatever operations the classes that
        are inheriting this class wants to perform.
        
        But the classes that are inheriting this class
        don't get to override run() method directly.
        
        They can override these methods:
        
        on_start()
        - This method is called before thread loop begins
        
        on_stepped()
        - This method is called inside the thread loop,
        - The code that is supposed to run again and again should
          be inside this method.
        - Method exit() can be called to exit the thread loop inside
          this method
        - Method terminate() can be called to terminate the thread
          upon encountering any kind of error or exceptions
        
        on_exit()
        - This method is called when the thread loop ends.
        
        on_terminated()
        - This method is called when the thread is abnormally terminated.
    
    """

    @abstractmethod
    def on_start(self):
        pass

    @abstractmethod
    def on_stepped(self):
        pass

    @abstractmethod
    def on_exit(self):
        pass

    @abstractmethod
    def on_terminated(self):
        pass

    """
    
        I think you already know how it works,
        but here's a small recap
        
        We are overriding run() Method from Thread.
        
        When thread starts,
        we will run on_start()
        
        After it finishes running, we will run
        on_stepped() inside the loop until the
        child class calls pyper_thread_exit() 
        method to stop running.
        
        Just before the thread ends,
        on_finished() is ran.
       
        If there is an abnormal termination,
        we will call on_terminated() to let
        the class perform clean up operations.
        
    """

    # overridden from Thread
    def run(self):
        self.on_start()

        while self._Running:
            self.on_stepped()

        self.on_exit()

    """
    
        Once the child class has finished his job,
        it has to exit itself from the loop.
        
        Hence, calling this method will break
        out of the loop.
    
    """

    def exit_pyper_thread(self):
        self._Running = False

    """
    
        If the child class faces some exceptions,
        it might have to exit abnormally.
        
        If you remember the pipelining pattern we have,
        if one of them terminates abnormally, other
        threads will also have to stop. calling
        terminate(String ErrorMessage) will take
        care of that for us.
        
        ErrorMessage will be printed on the console.
    
    """

    def terminate(self, error_message: str = "Thread Terminated"):
        print(error_message)

        self.cancel()

    """
    
        cancel() is called by terminate()
        to accomplish what terminate
        wants to accomplish
    
        A side note: cancel can also be used
        to silently terminate the threads, without
        printing error on console. Now you know.
        
    """

    def cancel(self):
        # kill current thread
        self.exit_pyper_thread()

        # Spawn a task to terminate other threads
        asyncio.create_task(self._terminate_connected_threads())

        # allow the class to clean up
        self.on_terminated()

    """
    
        _terminate_connected_threads() is 
        spawned to concurrently termiante
        all connected threads in the pipeline.
    
    """

    async def _terminate_connected_threads(self):

        if self._Next is not None:
            next_node = self._Next
            self._Next = None
            next_node.cancel()

        if self._Last is not None:
            last = self._Last
            self._Last = None
            last.cancel()
