#!/usr/bin/python3
"""BaseModel class unit tests"""
import io
import unittest
import uuid
from contextlib import redirect_stdout
from datetime import datetime
from pycodestyle import Checker
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test class for BaseModel """
    def test_pep8_compliance(self):
        """ Test that code conforms to pep8 style """
        files_to_check = [
                'models/base_model.py',
                'tests/test_models/test_base_model.py'
                ]

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            style = Checker(paths=files_to_check)
            result = style.check_all()

        output = stdout.getvalue().strip()
        self.assertFalse(output, f"PEP8 violations found:\n{output}")

    def test_attributes_type(self):
        """ Test to verify the attribute data types """
        new_object = BaseModel()
        new_object_id = uuid.UUID(new_object.id)

        self.assertIsInstance(new_object_id, uuid.UUID)
        self.assertIsInstance(new_object.created_at, datetime)
        self.assertIsInstance(new_object.updated_at, datetime)

    def test_str_representation(self):
        """ String representation test """
        new_obj = BaseModel()

        self.assertEqual(str(new_obj), "[{}] ({}) {}".format(
            new_obj.__class__.__name__, new_obj.id, new_obj.__dict__))

    def test_save(self):
        """ Save method test/check """
        new_obj = BaseModel()

        initial_time = new_obj.updated_at
        new_obj.save()
        latest_time = new_obj.updated_at

        self.assertNotEqual(initial_time, latest_time)
        self.assertTrue(latest_time > initial_time)
        self.assertIsInstance(latest_time, datetime)
        self.assertIsInstance(initial_time, datetime)


if __name__ == '__main__':
    unittest.main()
