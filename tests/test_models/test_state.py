#!/usr/bin/python3
"""Contain tests for the state module."""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test the State class."""

    def test_default_attributes(self):
        """Test for attributes."""

        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
