#!/usr/bin/python3
"""
Contain tests for the review module.
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the review class."""

    def test_default_attributes(self):
        """Test for attributes."""

        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
