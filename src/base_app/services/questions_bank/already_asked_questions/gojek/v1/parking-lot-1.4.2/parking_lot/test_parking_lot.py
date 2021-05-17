import unittest
from parking_lot import *
# import mycode


class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    def test_create_parking_lot(self):
        self.assertEqual(hello_world(), 'hello world')
