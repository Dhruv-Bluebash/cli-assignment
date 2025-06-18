# test_parser.py
import unittest
from parser import is_valid_row

class TestParser(unittest.TestCase):
    def test_valid_row(self):
        row = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'address': '123 Street',
            'city': 'City',
            'state': 'State',
            'postcode': '12345'
        }
        self.assertTrue(is_valid_row(row))

    def test_invalid_row(self):
        row = {
            'email': '',
            'first_name': 'John',
            'last_name': '',
            'address': '',
            'city': 'City',
            'state': 'State',
            'postcode': ''
        }
        self.assertFalse(is_valid_row(row))

if __name__ == '__main__':
    unittest.main()
