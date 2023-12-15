#!/usr/bin/python3

import unittest
from models.state import State


class test_state(unittest.TestCase):
    def test_attributes(self):
        state = State()

        self.assertEqual(state.name, "")
