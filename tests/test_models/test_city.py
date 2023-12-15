#!/usr/bin/python3

import unittest
from models.city import City


class test_city(unittest.TestCase):
    def test_attributes(self):
        city = City()

        self.assertEqual(city.name,  "")
