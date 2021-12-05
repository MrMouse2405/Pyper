from queue import Queue

from PyperFramework.Pyper_Thread import PyperThread
from PyperFramework.Phases.Phase_1_File_Reader import Phase1FileReader
from PyperFramework.Phases.Phase_2_SRC_To_AST import Phase2SRCToAST

"""

  Pyper Pipeline

  
  Pyper increases performance by using the multithreading pattern
  of pipelining. Each Python Source file (While Compilation) gets
  its own pipeline to process it.
 
  So compiling multiple files gets really fast as each file gets
  a set of threads dedicated to it.
 
  While it speeds up compilation of multiple files, but it also
  speeds up compilation of a file. As mentioned above, pyper uses
  pipelining, which means, it doesn't read the file, then parse it,
  and then optimize and compile it step by step.
 
  It does all of it simultaneously, the first thread reads the file,
  second parses the previously read line, and passes it to the next
  thread.

  For example:

  No pipelining:
 
  A file with 100 lines -> read all 100 -> parse all 100 -> compile all hundress
 
  With Pipelining:
 
  Read one -> pass it to next thread -> parse it -> pass it -> compile it
 
  This makes pyper faster because while the second thread is parsing the
  previously read line, the first thread reads a new one, saving time, and
  increasing performance.
 
  This class establishes this pipelining.

"""


def initialize(*args: PyperThread) -> list:
    thread_pool = []
    length = len(args) - 1

    for x in args:
        thread_pool.append(x)

    # Now connecting threads, Note, this is not a bitwise shift, we are using magic methods to look simple
    # A >> B means A's next is B, and A << B means A's last is B

    for x in range(length + 1):
        if x == 0:
            thread_pool[0].connect_next(thread_pool[1])
            thread_pool[1].connect_last(thread_pool[0])
        elif x == length:
            thread_pool[length].connect_last(thread_pool[length-1])
            thread_pool[length-1].connect_next(thread_pool[length])
        else:
            thread_pool[x - 1].connect_next(thread_pool[x])
            thread_pool[x].connect_last(thread_pool[x - 1])
            thread_pool[x].connect_next(thread_pool[x + 1])
            thread_pool[x + 1].connect_last(thread_pool[x])

    return thread_pool


class PyperPipeLine:

    def __init__(self, python_file):
        self._Phase1Queue = Queue()
        self._Phase2Queue = Queue()

        self.thread_pool: list[PyperThread] = initialize(
            Phase1FileReader(self._Phase1Queue, python_file),
            Phase2SRCToAST(self._Phase1Queue, self._Phase2Queue))


        for x in self.thread_pool:
            x.start()

        for x in self.thread_pool:
            x.join()

