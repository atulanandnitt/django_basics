# TO run UTs
# (questionBank) b2babu@b2babu:~/Documents/django_basics/src$ python manage.py test test.test_api

from rest_framework.test import APIClient
from unittest import TestCase

class TestOpps(TestCase):

    def test_opps1(self) -> bool:
        request = {
            "a": 10,
            "b": 20,
            "c": 30
        }
        test_obj = APIClient()
        res = test_obj.post(path='/summation', data=request, format='json')
        calculated_output_code = res.status_code
        expected_output_code = 200
        
        calculated_output = res.data
        expected_output = 60
        print("calculated_output", calculated_output)
        self.assertTrue(expected_output_code == calculated_output_code)
        # self.assertTrue(expected_output == calculated_output)