"""Test for the file_storage module"""
import models
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine import file_storage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the File Storage class"""

    def test_module_docstring(self):
        """Test for length of module docstring"""
        self.assertTrue(len(file_storage.__doc__) > 1)

    def test_class_docstring(self):
        """Test for length of class docstring"""
        self.assertTrue(len(FileStorage.__doc__) > 1)

    def test_filepath(self):
        """Test case for the storage file path"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        f1 = FileStorage()
        with self.assertRaises(AttributeError):
            _ = f1.__file_path

    def test_objects(self):
        """Test case for the objects dict"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        f1 = FileStorage()
        with self.assertRaises(AttributeError):
            _ = f1.__objects

    def test_all(self):
        """Test case for the all method"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """Test case for the new method"""
        base = BaseModel()
        user = User()
        city = City()
        place = Place()
        storage.new(base)
        storage.new(city)
        storage.new(user)
        storage.new(place)
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn("Place." + place.id, models.storage.all().keys())

    def test_save(self):
        """Test case for the save method"""
        base = BaseModel()
        user = User()
        city = City()
        place = Place()
        storage.new(base)
        storage.new(city)
        storage.new(user)
        storage.new(place)
        storage.save()
        with open("file.json", "r") as f:
            file_text = f.read()
        self.assertIn("BaseModel." + base.id, file_text)
        self.assertIn("User." + user.id, file_text)
        self.assertIn("City." + city.id, file_text)
        self.assertIn("Place." + place.id, file_text)


    def test_reload(self):
        """Test case for the reload method"""
        base = BaseModel()
        user = User()
        city = City()
        place = Place()
        storage.new(base)
        storage.new(city)
        storage.new(user)
        storage.new(place)
        storage.save()
        storage.reload()
        json_objects = storage.all()
        self.assertIn("BaseModel." + base.id, json_objects)
        self.assertIn("User." + user.id, json_objects)
        self.assertIn("City." + city.id, json_objects)
        self.assertIn("Place." + place.id, json_objects)


if __name__ == "__main__":
    unittest.main()
