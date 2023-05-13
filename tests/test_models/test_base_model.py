#!/usr/bin/python3
"""
Contain tests for the BaseModel class.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests attributes of the base model."""

    def test_create_instance_from_dict(self):
        """Test for attributes."""

        base_model = BaseModel()
        base_model.name = "My_First_Model"
        base_model.my_number = 89
        base_model_dict = base_model.to_dict()
        new_base_model = BaseModel(**base_model_dict)
        self.assertEqual(base_model.id, new_base_model.id)
        self.assertEqual(base_model.name, new_base_model.name)
        self.assertEqual(base_model.my_number, new_base_model.my_number)
        self.assertEqual(base_model.created_at, new_base_model.created_at)
        self.assertEqual(type(base_model.created_at), datetime)
        self.assertEqual(base_model.updated_at, new_base_model.updated_at)
        self.assertEqual(type(base_model.updated_at), datetime)


if __name__ == "__main__":
    unittest.main()
