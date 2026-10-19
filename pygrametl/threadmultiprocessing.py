"""Thread based stand-ins for the parts of the multiprocessing module that
pygrametl uses. They are used on CPython when the GIL is disabled (free-threaded
builds), where threads can run in parallel and avoid the cost of sending data
between processes. Jython uses jythonmultiprocessing instead.
"""

import queue
import threading

__all__ = ["JoinableQueue", "Process", "Queue", "Value"]


class Process(threading.Thread):
    pid = "<n/a>"


class Queue(queue.Queue):
    def close(self):
        pass


class JoinableQueue(Queue):
    pass


class Value(object):
    def __init__(self, typecode, value=0):
        self.value = value