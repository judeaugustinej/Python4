#!/bin/env python
# -*- coding: utf-8 -*-

"""
A program that imports a module and then goes through the module's namespace to find any functions 
and print the names of the functions and their arguments, in the same way as it might appear 
in a def statement.
"""
import os
import inspect

for f in inspect.getmembers(os, inspect.isfunction):
    func_name = f[0]
    func = getattr(os, func_name)
    print(func_name + inspect.formatargspec(*inspect.getfullargspec(func)))
