#!/usr/bin/python3
"""
This is FileStorage test module.
"""

import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Testing the FileStorage class
    """
    
    def setUp(self):
        """Initializing classes"""
        self.storage = FileStorage()
        self.bm = BaseModel()
        self.bm.name = "test"
        self.bm.my_number = 89
    
    def tearDown(self):
        """Clean up files created by tests
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        
    def test_all(self):
        """Test the all() method
        """
        objs = self.storage.all()
        self.assertIsInstance(objs, dict)
        
    def test_new(self):
        """Test the new() method
        """
        self.storage.new(self.bm)
        objs = self.storage.all()
        key = self.bm.__class__.__name__ + "." + self.bm.id
        self.assertIn(key, objs)
        
    def test_save(self):
        """Test the save() method
        """

        self.storage.new(self.bm)
        self.storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
            key = self.bm.__class__.__name__ + "." + self.bm.id
            self.assertIn(key, data)
        
    def test_reload(self):
        """Test the reload() method
        """
        self.storage.new(self.bm)
        self.storage.save()
        self.storage.reload()
        objs = self.storage.all()
        key = self.bm.__class__.__name__ + "." + self.bm.id
        self.assertIn(key, objs)
        
if __name__ == "__main__":
    unittest.main()