#!/bin/env python
# -*- coding: utf-8 -*-

"""
ctx_man.py: A context manager class that suppresses any ValueError exceptions that 
occur in the controlled suite, but allows any other exception to be raised in the 
surrounding context.
"""
from contextlib import contextmanager
@contextmanager
def ctx_man():
    try:
        yield
    except ValueError:
        "suppress any ValueError exceptions"
        pass
    except:
        "raise other exceptions"
        raise
    finally:
        pass

if __name__ == '__main__':
    "example that ValueError exception is suppressed"
    with ctx_man() as cm:
        x = int('one')
    
    "examples that any other exception except ValueError is allowed to raised"
    with ctx_man() as cm:
        x = 1 / 0
#        x = 'one' + 2
