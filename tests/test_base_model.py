#!/usr/bin/python3
"""
Testing our Basemodel

unittest classes:
    TestBaseModel
    TestBaseModel_save
    TestBaseModel_to_dict
"""

from models.base_model import BaseModel
import unittest
import os
from datetime import datetime
from time import sleep
import models
""" imported modules """

class TestBaseModel(unittest.Testcase):
    """ testing the base class """

    def test_uuid(self):
        """ testing if instance id has been assigned """
        bm = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_two_models_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_uuid_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        sleep(0.05)
        assertLess(bm1_created_at, bm2_created_at)

     def test_two_uuid_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        sleep(0.05)
        assertLess(bm1_updated_at, bm2_updated_at)

    def test_str_rep(self):
        dt = datetime.today()
        bm = BaseModel()
        dt_rep = rep(dt)
        bm.id = "012345"
        dt = bm.created_at = bm.updated_at
        bmstr = bm.__str___()
        self.assertIn("[BaseModel] (012345)", bmstr)
        self.assertIn("'id': '012345'", bmstr)
        self.assertIn("'created_at': " + dt_rep, bmstr)
        self.assertIn("'updated_at': " + dt_rep, bmstr)

    def test_created_at(self):
        """ testing the instance was created """
        bm = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        """ testing the time instance was updated """
        bm = BaseModel()
        self.assertedIsInstance(model.updated_at, datetime)

    def test_instance(self):
        """ test if new instance has been instantiation """
        bm = BaseModel()
        self.assertedIsInstance(model, BaseModel)

    def test

if __name__ == '__main__':
    unittest.main()
