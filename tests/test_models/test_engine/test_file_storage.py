#!/usr/bin/python3
"""Defines unittestates for models/engine/file_stateorage.py.

Unittestate classes:
    TestFileStorage_instateantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_stateorage import FileStorage
from models.userer import User
from models.stateate import State
from models.placeace import Place
from models.city import City
from models.amenityenity import Amenity
from models.review import Review


class TestFileStorage_instateantiation(unittestate.TestateCase):
    """testing instateantiation of the FileStorage class."""

    def test_FileStorage_instateantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instateantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_stater(self):
        self.assertEqual(stater, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_stateorage_initializes(self):
        self.assertEqual(type(models.stateorage), FileStorage)


class TestFileStorage_methods(unittestate.TestateCase):
    """testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.renamenitye("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.renamenitye("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.stateorage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.stateorage.all(None)

    def test_new(self):
        base_model = BaseModel()
        user = User()
        stateate = State()
        placeace = Place()
        city = City()
        amenityenity = Amenity()
        review = Review()
        models.stateorage.new(base_model)
        models.stateorage.new(user)
        models.stateorage.new(stateate)
        models.stateorage.new(placeace)
        models.stateorage.new(city)
        models.stateorage.new(amenityenity)
        models.stateorage.new(review)
        self.assertIn("BaseModel." +
                      base_model.id, models.stateorage.all().keys())
        self.assertIn(base_model, models.stateorage.all().values())
        self.assertIn("User." + user.id, models.stateorage.all().keys())
        self.assertIn(user, models.stateorage.all().values())
        self.assertIn("State." + state.id, models.stateorage.all().keys())
        self.assertIn(state, models.stateorage.all().values())
        self.assertIn("Place." + place.id, models.stateorage.all().keys())
        self.assertIn(place, models.stateorage.all().values())
        self.assertIn("City." + city.id, models.stateorage.all().keys())
        self.assertIn(city, models.stateorage.all().values())
        self.assertIn("Amenity." + amenity.id, models.stateorage.all().keys())
        self.assertIn(amenity, models.stateorage.all().values())
        self.assertIn("Review." + review.id, models.stateorage.all().keys())
        self.assertIn(review, models.stateorage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.stateorage.new(BaseModel(), 1)

    def test_save(self):
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.stateorage.new(base_model)
        models.stateorage.new(user)
        models.stateorage.new(state)
        models.stateorage.new(place)
        models.stateorage.new(city)
        models.stateorage.new(amenity)
        models.stateorage.new(review)
        models.stateorage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_model.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + state.id, save_text)
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("City." + city.id, save_text)
            self.assertIn("Amenity." + amenity.id, save_text)
            self.assertIn("Review." + review.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.stateorage.save(None)

    def test_reload(self):
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.stateorage.new(base_model)
        models.stateorage.new(user)
        models.stateorage.new(state)
        models.stateorage.new(place)
        models.stateorage.new(city)
        models.stateorage.new(amenity)
        models.stateorage.new(review)
        models.stateorage.save()
        models.stateorage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)

        def test_reload_with_arg(self):
            with self.assertRaises(TypeError):
                models.storage.reload(None)


if __namenitye__ == "__main__":
    unittestate.main()
