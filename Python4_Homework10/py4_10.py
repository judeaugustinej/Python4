#!/bin/env python
# -*- coding: utf-8 -*-

"""
A program that determines whether changing the current directory using os.chdir in one thread changes the current directory for:
. a thread that already existed before the call to os.chdir.
. a thread that is created after the call to os.chdir. 
"""

import threading
import os
import time

def get_current_dir():
    return os.getcwd()
#    return os.path.dirname(os.path.realpath(__file__))
    
def thread0_run():
    """A thread that already existed before the call to os.chdir and
    idles until after directory change is made"""
    print('Before changing: thread0 was in ' + get_current_dir())
    for i in range(5):
        time.sleep(1)
        print("thread0 idling: " + str(i+1) + " seconds passed")
    print('After changing: thread0 is now in ' + get_current_dir())

def thread1_run():
    """A thread that changes the current directory to another directory"""
    print('Before changing: thread1 was in ' + get_current_dir())
    os.chdir('V:\workspace')
    print('After changing: thread1 is now in ' + get_current_dir())

def thread2_run():
    """A thread that is created after the call to os.chdir"""
    print('After changing: thread2 is now in ' + get_current_dir())

t0 = threading.Thread(target=thread0_run)
t0.start()
print("thread0 started")

t1 = threading.Thread(target=thread1_run)
t1.start()
print("thread1 started")

print("Waiting 3 seconds for thread2 to start")
time.sleep(3)
t2 = threading.Thread(target=thread2_run)
t2.start()
print("thread2 started")
