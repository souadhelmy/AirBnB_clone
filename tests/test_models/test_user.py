#!/usr/bin/python3
"""
Contain tests for the user module.
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test the user class."""


    def test_default_attributes(self):
        """Test for attributes."""


        user = User()
        self.assertEqual(user.username, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.email, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
