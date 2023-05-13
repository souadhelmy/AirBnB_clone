#!/usr/bin/python3
"""Contain tests for the city module."""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test the city class."""

    def test_default_attributes(self):
        """Test for attributes."""

        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
