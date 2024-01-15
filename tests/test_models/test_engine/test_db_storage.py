#!/usr/bin/python3
""" Module for testing database storage"""
import unittest
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.engine.db_storage import DBStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class TestDBStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create an SQLite database in memory for testing
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=cls.engine)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()
        cls.db_storage = DBStorage()
        cls.db_storage.reload()

    @classmethod
    def tearDownClass(cls):
        # Close the session and clean up the database
        cls.session.close()

    def test_all_method(self):
        # Test the all method for DBStorage

        # Add some objects to the database
        user = User(email='test@example.com', password='password')
        state = State(name='TestState')
        self.db_storage.new(user)
        self.db_storage.new(state)
        self.db_storage.save()

        # Query all objects and check if they are present
        all_objects = self.db_storage.all()
        self.assertIn('User.' + user.id, all_objects)
        self.assertIn('State.' + state.id, all_objects)

        # Query only User objects and check if User object is present
        user_objects = self.db_storage.all(cls='User')
        self.assertIn('User.' + user.id, user_objects)
        self.assertNotIn('State.' + state.id, user_objects)

    def test_new_method(self):
        # Test the new method for DBStorage

        # Add an object to the database
        user = User(email='test@example.com', password='password')
        self.db_storage.new(user)
        self.db_storage.save()

        # Query the object and check if it is present
        queried_user = self.session.query(User).first()
        self.assertEqual(user, queried_user)

    def test_delete_method(self):
        # Test the delete method for DBStorage

        # Add an object to the database
        user = User(email='test@example.com', password='password')
        self.db_storage.new(user)
        self.db_storage.save()

        # Delete the object and check if it is not present in the database
        self.db_storage.delete(user)
        self.db_storage.save()
        queried_user = self.session.query(User).first()
        self.assertIsNone(queried_user)

    def test_reload_method(self):
        # Test the reload method for DBStorage

        # Create a new instance of DBStorage, which triggers the reload method
        new_db_storage = DBStorage()

        # Check if the tables are created correctly in the database
        self.assertTrue(self.engine.dialect.has_table(self.engine, 'users'))
        self.assertTrue(self.engine.dialect.has_table(self.engine, 'states'))
