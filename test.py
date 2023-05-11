# -*- coding: utf-8 -*-
"""
Created on Thu May 11 03:55:58 2023

@author: Lenovo
"""

import unittest
import numpy as np
from data_processing import calculate_slope, calculate_aspect

class TestSlopeAspect(unittest.TestCase):
    
    def setUp(self):
        # Initialize test data and cell size before each test function
        self.test_data = np.array([
            [10, 10, 10],
            [20, 20, 20],
            [30, 30, 30]
        ])
        self.cell_size = 1

    def test_calculate_slope(self):
        # Test the function calculate_slope
        result = calculate_slope(self.test_data, self.cell_size)
        expected_result = np.array([
            [10.0, 10.0, 10.0], 
            [10.0, 10.0, 10.0], 
            [10.0, 10.0, 10.0]
        ])
        
        # Check if the result is close to the expected result using np.allclose
        if not np.allclose(result, expected_result, rtol=1e-2):
            # Print an error message if the test fails
            print("test_calculate_slope failed:")
            print("result:")
            print(result)
            print("expected_result:")
            print(expected_result)
        # Use assertTrue to check if the result and expected_result are equal
        self.assertTrue(np.allclose(result, expected_result, rtol=1e-2))

    def test_calculate_aspect(self):
        # Test the function calculate_aspect
        result = calculate_aspect(self.test_data, self.cell_size)
        expected_result = np.array([
            [270.0, 270.0, 270.0], 
            [90.0, 90.0, 90.0], 
            [90.0, 90.0, 90.0]
            ])
        
        # Check if the result is close to the expected result using np.allclose
        if not np.allclose(result, expected_result, rtol=1e-2):
            # Print an error message if the test fails
            print("test_calculate_aspect failed:")
            print("result:")
            print(result)
            print("expected_result:")
            print(expected_result)
        # Use assertTrue to check if the result and expected_result are equal
        self.assertTrue(np.allclose(result, expected_result, rtol=1e-2))

if __name__ == '__main__':
    # Run all the test functions in the TestSlopeAspect class
    unittest.main()








    


