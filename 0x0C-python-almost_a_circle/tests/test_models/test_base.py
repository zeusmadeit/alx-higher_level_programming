#!/usr/bin/python3
"""Test file for Base model"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Base Test Class"""
    def test_base(self):
        a = Base()
        b = Base(5)
        self.assertEqual(a.id, 4)
        self.assertEqual(b.id, 5)
