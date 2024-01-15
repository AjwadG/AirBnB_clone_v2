#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
from datetime import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except IOError:
            pass

    def test_instance(self):
        """test instantisation"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test initialization with keyword arguments"""
        data = {
            "id": "sample_id",
            "created_at": "2022-01-01T12:00:00.000000",
            "updated_at": "2022-01-02T14:30:00.500000",
            "custom_attribute": "custom_value"
        }

        # Create an instance with the provided keyword arguments
        model_instance = BaseModel(**data)

        # Verify that instance variables are set correctly
        self.assertEqual(model_instance.id, "sample_id")
        self.assertEqual(model_instance.custom_attribute, "custom_value")

        # Verify that datetime attributes are parsed correctly
        expected_created_at = datetime.strptime("2022-01-01T12:00:00.000000",
                                                "%Y-%m-%dT%H:%M:%S.%f")
        expected_updated_at = datetime.strptime("2022-01-02T14:30:00.500000",
                                                "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(model_instance.created_at, expected_created_at)
        self.assertEqual(model_instance.updated_at, expected_updated_at)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)
