import pytest
from . import api3_toGetAllUsers
from . import api4_toGetDataOfParticularUser
from . import helperClassesForAPI_3_and_4
import http.client
import json
import random

def firstNameOfAllUsers(baseUrl, apiName):
    conn = http.client.HTTPConnection(baseUrl)
    headers = {
        'cache-control': "no-cache",
        'postman-token': "ed0b6cc7-f185-4f9a-d1c2-839beac55b5d"
    }
    pathParameter = "/" + apiName
    conn.request("GET", pathParameter, headers=headers)
    res = conn.getresponse()
    json_object_list = json.load(res)


    firstNameOfAllUsers = list()
    for item in json_object_list:
        try:
            firstNameOfAllUsers.append(item['first_name'])
        except:
            print("empty row in DB")

    return firstNameOfAllUsers



def test_restCall_4_1():
    """
    Positive test case: just validate each json object has 6 keys
    :return:
    """
    baseUrl = "54.191.230.109:443"
    apiNameToGetAllUsers = "users"
    allUserNames = ["Eve", "Charles"]#firstNameOfAllUsers(baseUrl, apiNameToGetAllUsers)
    noOfTestCases = 2
    randomIndexes = [0,1]#random.sample(range(0, len(allUserNames)), noOfTestCases)
    apiName = "user"

    hc4 = helperClassesForAPI_3_and_4.HelperClassesForAPI_4()

    for i in randomIndexes:

        result = api4_toGetDataOfParticularUser.restCall_4(baseUrl, apiName, allUserNames[i])
        assert (True == hc4.isJsonHasSpecificFourKeys(result))


def test_restCall_4_2():
    """
    Positive test case: validate the data type of
     each keys of each json object
    :return:
    """
    baseUrl = "54.191.230.109:443"
    apiNameToGetAllUsers = "users"
    allUserNames = ["Eve", "Charles"]#firstNameOfAllUsers(baseUrl, apiNameToGetAllUsers)
    noOfTestCases = 2
    randomIndexes = [0,1]#random.sample(range(0, len(allUserNames)), noOfTestCases)
    apiName = "user"

    hc4 = helperClassesForAPI_3_and_4.HelperClassesForAPI_4()

    for i in randomIndexes:

        result = api4_toGetDataOfParticularUser.restCall_4(baseUrl, apiName, allUserNames[i])
        assert (True == hc4.isJsonHasSpecificFourKeys(result))
        assert (True == hc4.isAllJsonFormateAreCorrect_3_and_4(result))


