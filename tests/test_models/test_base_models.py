#!/usr/bin/python3
""" MY TESTCASE FOR THE BASE MODEL """

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ FUNCTION TO TEST BASEMODEL """

    def test_init(self):
        """Tests that BaseModel instance is initialized correctly."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Tests the string representation of a BaseModel instance."""
        model = BaseModel()
        model.id = "abcd-1234"
        model.created_at = datetime(2024, 2, 11, 20, 22, 0)
        expected_str = "[BaseModel] (abcd-1234) {'id': 'abcd-1234', ..."
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """Tests that the save method updates the updated_at attribute."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Tests that the to_dict method returns a correct dictionary."""
        model = BaseModel()
        model.id = "abcd-1234"
        model.created_at = datetime(2024, 2, 11, 20, 22, 0)
        model.updated_at = datetime(2024, 2, 12, 10, 30, 0)
        expected_dict = {
            "__class__": "BaseModel",
            "id": "abcd-1234",
            "created_at": "2024-02-11T20:22:00.000000",
            "updated_at": "2024-02-12T10:30:00.000000",
        }
        self.assertDictEqual(model.to_dict(), expected_dict)

if __name__ == "__main__":
    unittest.main()
