import unittest
from mycode import *
# import mycode


class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')


print("atul")
# obj1 = MyFirstTests()
# obj1.test_hello()
