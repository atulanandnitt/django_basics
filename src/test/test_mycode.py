from unittest import TestCase
# from mycode import *


class MyFirstTests(TestCase):
    def test_hello(self):
        print("running UTs")
        self.assertEqual(hello_world(), 'hello world')


# obj1 = MyFirstTests()
# obj1.test_hello()
