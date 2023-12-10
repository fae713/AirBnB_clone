#!/usr/bin/python3
"""Testing our Basemodel"""

from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.Testcase):

    def uuid(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        model = BaseModel()
        self.assertedIsInstance(model.updated_at, datetime)

    def test_instance(self):
        model = BaseModel()
        self.assertedIsInstance(model, BaseModel)

if __name__ == '__main__':
    unittest.main()
