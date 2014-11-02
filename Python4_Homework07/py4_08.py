#!/bin/env python
# -*- coding: utf-8 -*-

"""
A program that uses timeit() to show the difference between a list comprehension 
and the list() function applied to:
- a list of a million random numbers.
- a generator that generates a sequence of a million random numbers. 
"""
from random import random
from timeit import timeit
MILLION = 1000000
TRY_NUM = 10

lst = list(random() for j in range(MILLION))

print("Test case 1: applied to a list of a million random numbers")
print("List comprehension: ", timeit("sum([x for x in lst])", "from __main__ import lst", number=TRY_NUM))
print("List() function: ", timeit("sum(list(x for x in lst))", "from __main__ import lst", number=TRY_NUM))

gen = [random() for j in range(MILLION)]
print("Test case 2: applied to a generator that generates a sequence of a million random numbers")
print("List comprehension: ", timeit("sum([x for x in gen])", "from __main__ import gen", number=TRY_NUM))
print("List() function: ", timeit("sum(list(x for x in gen))", "from __main__ import gen", number=TRY_NUM))
