#!/usr/bin/python3
"""Contain tests for the amenity module."""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
   """Test the amenity class."""

def test_default_attributes(self):
    """Test for attributes."""


    amenity = Amenity()
    self.assertEqual(amenity.name, "")


if __name__ == "__main__":      
  unittest.main()