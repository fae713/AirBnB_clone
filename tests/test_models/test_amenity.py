#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    def test_attribute(self):
        amenity = Amenity()

        self.assertEqual(amenity.name, "")
