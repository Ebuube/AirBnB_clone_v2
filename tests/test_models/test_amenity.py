#!/usr/bin/python3
"""
Tests for the Amenity model
"""
import unittest
import models
from tests.test_models.test_base_model import test_BaseModel
from models.amenity import Amenity
from sqlalchemy import Column
from sqlalchemy.orm import relationship


class test_Amenity(test_BaseModel):
    """
    Define extra tests for the ``Amenity`` class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the class' test
        """
        super().__init__(*args, **kwargs)
        self.value = Amenity
        self.name = self.value.__name__

    def setUp(self):
        """
        Set up for tests
        """
        super().setUp()

    def tearDown(self):
        """
        Tear down for the tests
        """
        super().tearDown()

    @unittest.skipUnless(models.storage_type == 'file', "Using file storage")
    def test_user_attrs(self):
        """
        Ensure that the correct attributes are present in the model
        Namely:
        - name -> string
        """
        _cls = Amenity

        foo = _cls()
        attrs = {'name': str}

        for attr, attr_type in attrs.items():
            with self.subTest(attr=attr, attr_type=attr_type):
                self.assertTrue(hasattr(foo, attr))
                self.assertTrue(type(getattr(foo, attr)) is attr_type)
