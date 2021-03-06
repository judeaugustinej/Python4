#!/bin/env python
# -*- coding: utf-8 -*-

"""
Test 3D-array implementations using tuple subscripting.
"""
import unittest
import arr

class TestArray(unittest.TestCase):
    
    def test_zeroes(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], 0)
    
    def test_identity(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                a[i, i, i] = 1
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], i == j and j == k)
    
    def _index(self, a, x, y, z):
        return a[x, y, z]
    
    def test_key_validity(self):
        a = arr.array(5, 5, 5)
        self.assertRaises(KeyError, self._index, a, -1, 3, 4)
        self.assertRaises(KeyError, self._index, a, 2, 3, 10)
        
if __name__ == '__main__':
    unittest.main()
