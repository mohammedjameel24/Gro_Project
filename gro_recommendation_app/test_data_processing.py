#python
# Import necessary libraries
import unittest
import pandas as pd
import numpy as np
from data_processing import process_data

class TestDataProcessing(unittest.TestCase):
    """
    This class tests the data processing function in data_processing.py
    """

    def setUp(self):
        """
        This method sets up the test data to be used in the test cases.
        """
        self.user_data = {
            'age': 25,
            'income': 50000,
            'gender': 'Male',
            'occupation': 'Engineer'
        }

    def test_process_data(self):
        """
        This method tests the process_data function.
        """
        # Process the test data
        processed_data = process_data(self.user_data)

        # Check that the output is a DataFrame
        self.assertIsInstance(processed_data, pd.DataFrame)

        # Check that the scaled columns have a mean of 0 and a standard deviation of 1
        self.assertAlmostEqual(processed_data['age'].mean(), 0)
        self.assertAlmostEqual(processed_data['age'].std(), 1)
        self.assertAlmostEqual(processed_data['income'].mean(), 0)
        self.assertAlmostEqual(processed_data['income'].std(), 1)

        # Check that the categorical columns have been converted to dummy variables
        self.assertIn('gender_Male', processed_data.columns)
        self.assertIn('occupation_Engineer', processed_data.columns)

if __name__ == '__main__':
    unittest.main()

