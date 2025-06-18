# test_geo.py
import unittest
from geo import get_coordinates

class TestGeo(unittest.TestCase):
    def test_valid_address(self):
        coords = get_coordinates("12-26 Argyle Street, SYDNEY, NSW, 2000")
        self.assertIsNotNone(coords)
        self.assertIsInstance(coords, tuple)

if __name__ == '__main__':
    unittest.main()
