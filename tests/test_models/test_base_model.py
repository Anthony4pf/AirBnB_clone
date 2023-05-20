"""Testing the base model module"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models import base_model
import time
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Test Cases for BaseModel class"""

    def test_module_docstring(self):
        """Test for len of module docstring"""
        self.assertTrue(len(base_model.__doc__) > 1)

    def test_class_docstring(self):
        """Test for class docstring"""
        self.assertTrue(len(BaseModel.__doc__) > 1)

    def test_initialization(self):
        """Test the init of the BaseModel class"""
        b1 = BaseModel()
        uuid_2 = str(uuid.uuid4)
        b2 = BaseModel(name="Anthony", club="Barcelona", id=uuid_2)
        uuid_1 = str(b1.id)
        self.assertNotEqual(uuid_1, uuid_2)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)
        self.assertEqual("Anthony", b2.name)
        self.assertEqual("Barcelona", b2.club)

    def test_save(self):
        """Test the save method of the BaseModel class"""
        b1 = BaseModel()
        old_updated_date = b1.updated_at
        old_date = b1.created_at
        time.sleep(1)
        b1.save()
        new_updated_date = b1.updated_at
        new_date = b1.created_at
        self.assertNotEqual(old_updated_date, new_updated_date)
        self.assertEqual(old_date, new_date)

    def test_str(self):
        """Test the str method"""
        b1 = BaseModel()
        str_string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        self.assertEqual(str_string, b1.__str__())

    def test_to_dict(self):
        """Test to_dict method"""
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertIn("id", b1_dict.keys())
        self.assertIn("created_at", b1_dict.keys())
        self.assertIn("updated_at", b1_dict.keys())
        self.assertIn("__class__", b1_dict.keys())
        self.assertEqual(b1_dict["__class__"], type(b1).__name__)


if __name__ == '__main__':
    unittest.main()
