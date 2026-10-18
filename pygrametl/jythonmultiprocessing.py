"""A module emulating (a small part of) CPython's multiprocessing with threads.
With this, pygrametl can be made to use multiprocessing, but actually use
threads. This is always the case on Jython (where there is no GIL). On CPython,
it is used when the environment variable PYGRAMETL_THREADS is set to 1, which
is intended for free-threaded builds where threads can run in parallel.
"""

# Copyright (c) 2011-2020, Aalborg University (pygrametl@cs.aau.dk)
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# - Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.

# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys 
from threading import Thread

try:
    from pygrametl.jythonsupport import Value # A Java class, only on Jython 
except ImportError:

    class Value(object):
        """Stands in for multiprocessing. Value when used on Cpython."""

        def __init__(self, typecode, value=0):
            self.value = value

# Needed for both pip2 and pip3 to be supported
try:
    from Queue import Queue
except ImportError:
    from queue import Queue

# NOTE: This module is made for Jython and is also used for threads on Cpython.

__all__ = ["JoinableQueue", "Process", "Queue", "Value"]


class Process(Thread):
    pid = "<n/a>"
    if sys.platform.startswith("java"):
        daemon = property(Thread.isDaemon, Thread.setDaemon)
        name = property(Thread.getName, Thread.setName)


class JoinableQueue(Queue):
    def close(self):
        pass
