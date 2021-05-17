import pytest
from . import api5_toANewUserIntoDB
import random
def payloadGenerator():
    payload = """{
                "id": """ + str(random.randint(111,999))+ """,
                "first_name": "avenger",
                "last_name": "bravos",
                "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/bigmancho/128.jpg"
                }"""
    return payload



def test_restCall_5_1():
    baseUrl = "54.191.230.109:443"
    apiName = "user"
    payload = payloadGenerator()
    result = api5_toANewUserIntoDB.restCall_5(baseUrl, apiName, payload)
    assert (result == 200)



def test_restCall_5_2():
    baseUrl = "54.191.230.109:443"
    apiName = "user"
    payload = payloadGenerator()
    result = api5_toANewUserIntoDB.restCall_5(baseUrl, apiName, payload)
    assert (result == 200)

def test_restCall_5_3():
    baseUrl = "54.191.230.109:443"
    apiName = "user"
    payload = payloadGenerator()
    result = api5_toANewUserIntoDB.restCall_5(baseUrl, apiName, payload)
    assert (result == 200)

def test_restCall_5_4():
    baseUrl = "54.191.230.109:443"
    apiName = "user"
    payload = payloadGenerator()
    result = api5_toANewUserIntoDB.restCall_5(baseUrl, apiName, payload)
    assert (result == 200)