import pytest
from . import api3_toGetAllUsers
from . import helperClassesForAPI_3_and_4

sampleJson = [{
    "id": "121212",
    "first_name": "string",
    "last_name": "string",
    "avatar": "string"
}]


def test_restCall_3():
    baseUrl = "54.191.230.109:443"
    apiName = "users"


    hc3 = helperClassesForAPI_3_and_4.HelperClassesForAPI_3()

    result = api3_toGetAllUsers.restCall_3(baseUrl, apiName)
    if result:
        assert (True == hc3.isEachJsonOfArrayHasSpecificFourKeys_3(result))
        assert (True == hc3.isEachJsonOfTheArrayHasCorrectDataFormate_3(result))