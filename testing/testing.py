# Example 1
# Using the unittest module for TestCase and UnitTest

import unittest
from tests import get_formatted_name


class NameTestCase(unittest.TestCase):
    '''Tests for "test.py".'''

    def test_first_last_name(self):
        """Do names like 'Okeke Okafor' work?"""
        formatted_name = get_formatted_name('okeke', 'okafor')
        self.assertEqual(formatted_name, 'Okeke Okafor')

    def test_first_last_middle_name(self):
        """Do names like 'Okeke Okafor Okonkwo' work?"""
        formatted_name = get_formatted_name('okeke', 'okafor', 'okonkwo')
        self.assertEqual(formatted_name, 'Okeke Okonkwo Okafor')


if __name__ == "__main__":
    unittest.main()
