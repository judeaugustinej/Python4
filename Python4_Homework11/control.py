#!/bin/env python
# -*- coding: utf-8 -*-

"""
control.py: Creates queues, starts output and worker threads,
            and pushes inputs into the input queue.
"""
from queue import Queue
from output import OutThread
from worker import WorkerThread
import random
import string
from timeit import timeit

def run():
    WORKERS = 10
    
    inq = Queue(maxsize=int(WORKERS*1.5))
    outq = Queue(maxsize=int(WORKERS*1.5))
    
    ot = OutThread(WORKERS, outq)
    ot.start()
    
    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()
    
    # generate a random string of alphabetic characters of length one thousand
    instring = (''.join(random.choice(string.ascii_letters) for i in range(1000)))
    
    for work in enumerate(instring):
        inq.put(work)
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    print("Control thread terminating")

print("Program runtime: ", timeit("run()", "from __main__ import run", number=1))
