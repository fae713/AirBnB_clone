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

class TestBaseModel(unittest.TestCase):
    """ testing the base class """
    def test_attributes(self):
        bm = BaseModel()
        self.assertTrue(hasattr(self.bm, 'id'))
        self.assertTrue(hasattr(self.bm, 'created_at'))
        self.assertTrue(hasattr(self.bm, 'updated_at'))

    def test_unique_id(self):
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
        self.assertIsInstance(model.updated_at, datetime)

    def test_instance(self):
        """ test if new instance has been instantiation """
        bm = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_save:
        bm = BaseModel()
        first_updated_at = bm.updated_at
        time.sleep(0.05)
        bm.save()
        self.assertNotEqual(bm.updated_at, first_updated_at)

    def test_to_dict(self):
        bm = BaseModel()
        obj_dict = bm.to_dict()
        expected_keys = {'id', 'created_at', 'updated_at', '__class__'}
        self.assertTrue(set(obj_dict.keys()) == expected_keys)
        self.assertEqual(obj_dict['__class__'], bm.__class__.__name__)
        self.assertEqual(obj_dict['created_at'], bm.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], bm.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
