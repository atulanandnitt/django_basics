import pytest
from . import api6_deleteParticularUser
import random

def payloadGenerator():
    payload = """{
                }"""
    return payload



def test_restCall_6_1():
    """
    Positive Test case
    :return:
    """
    baseUrl = "54.191.230.109:443"
    apiName = "user"
    userName = "avenger"
    payload = payloadGenerator()
    result = api6_deleteParticularUser.restCall_6(baseUrl, apiName, userName, payload)
    assert (result == 200)



def test_restCall_6_2():
    """
    Positive test case
    :return:
    """
    baseUrl = "54.191.230.109:443"
    apiName = "user"
    userName = "Eve"
    payload = payloadGenerator()
    result = api6_deleteParticularUser.restCall_6(baseUrl, apiName, userName, payload)
    assert (result == 200)

def test_restCall_6_3():
    """
    Negative Test Case
    userName = "RandomNameWhichIsNotInTheDB" : which cant be deleted
    :return:
    """
    baseUrl = "54.191.230.109:443"
    apiName = "user"
    userName = "RandomNameWhichIsNotInTheDB"
    payload = payloadGenerator()
    result = api6_deleteParticularUser.restCall_6(baseUrl, apiName, userName, payload)
    assert (result != 200)


def test_restCall_6_4():
    """
    This function is Negative Test Case
    :return:
    """
    baseUrl = "54.191.230.109:443"
    apiName = "user"
    userName = "Atul"
    payload = payloadGenerator()
    result = api6_deleteParticularUser.restCall_6(baseUrl, apiName, userName, payload)
    assert (result != 200)