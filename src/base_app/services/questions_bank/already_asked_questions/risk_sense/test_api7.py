import pytest
from . import api7_ToUpdateSpecificUser
import random

def payloadGenerator():
    payload = """{
                "id": """ + str(random.randint(111,999))+ """,
                "first_name": "avenger",
                "last_name": "bravos",
                "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/bigmancho/128.jpg"
                }"""
    return payload

def payloadGenerator2():
    payload = "{\r\n              " \
              "\"id\": 555,\r\n    " \
              "\"first_name12\": \"atul\",\r\n  " \
              "\"last_name123\": \"anand\",\r\n " \
              "\"avatar\": \"https://s3.amazonaws.com/uifaces/faces/twitter/bigmancho/128.jpg\"\r\n                }"
    return payload


def test_restCall_6_1():
    """
    Positive test case: Update a existing data
    :return:
    """

    baseUrl = "54.191.230.109:443"
    apiName = "user"
    userName = "avenger"
    payload = payloadGenerator()
    result = api7_ToUpdateSpecificUser.restCall_7(baseUrl, apiName, userName, payload)
    assert (result == 200)



def test_restCall_6_2():
    """
    Positive test case: Update a existing data by using different payload generator
    :return:
    """
    baseUrl = "54.191.230.109:443"
    apiName = "user"
    userName = "Eve"
    payload = payloadGenerator2()
    result = api7_ToUpdateSpecificUser.restCall_7(baseUrl, apiName, userName, payload)
    assert (result == 200)

def test_restCall_6_3():
    """
    Negative Test Case
    userName = "RandomNameWhichIsNotInTheDB"
    :return:
    """

    baseUrl = "54.191.230.109:443"
    apiName = "user"
    userName = "RandomNameWhichIsNotInTheDB"
    payload = payloadGenerator()
    result = api7_ToUpdateSpecificUser.restCall_7(baseUrl, apiName, userName, payload)
    assert (result != 200)


def test_restCall_6_4():
    """
    userName = some special charecters eg : "#@$#$%#$dsfads34"
    :return:
    """
    baseUrl = "54.191.230.109:443"
    apiName = "user"
    userName = "#@$#$%#$dsfads34"
    payload = payloadGenerator()
    result = api7_ToUpdateSpecificUser.restCall_7(baseUrl, apiName, userName, payload)
    assert (result != 200)