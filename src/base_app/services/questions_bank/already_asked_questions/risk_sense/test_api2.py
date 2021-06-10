import pytest
from . import api2_toGetArrayOfJsonObjectsOfSpecificType
from . import helperClasses


sampleJson = [{
    "type": "blindferret",
    "description": "Project Blindferret zmap scanners",
    "name": "Blindferret",
    "lastupdate": "2018-12-05 09:24:19",
    "datatype": "is_ipv4",
    "frequency": "0"
}]


def test_restCall_2_1():
    baseUrl = "54.191.230.109:443"
    apiName = "threatfeed"

    positiveTestCases__AllTypesOfAPIs = [ "blocklistde21", "blocklistde22", "blocklistde25"]

    hc = helperClasses.HelperClasses2()

    for typeAPI in positiveTestCases__AllTypesOfAPIs:

        result = api2_toGetArrayOfJsonObjectsOfSpecificType.restCall_2(baseUrl, apiName, typeAPI)
        if result:

            assert (typeAPI == result[0]["type"])

            assert (sampleJson[0].keys() == hc.isAllJsonSpecificSixKeys(result))

            assert(True == hc.isAllJsonFormateAreCorrect_1_and_2(result) )


def test_restCall_2_2():
    baseUrl = "54.191.230.109:443"
    apiName = "threatfeed"

    positiveTestCases__AllTypesOfAPIs = ["blindferret", "blocklistde110", "blocklistde143"]

    hc = helperClasses.HelperClasses2()

    for typeAPI in positiveTestCases__AllTypesOfAPIs:

        result = api2_toGetArrayOfJsonObjectsOfSpecificType.restCall_2(baseUrl, apiName, typeAPI)
        if result:

            assert (typeAPI == result[0]["type"])

            assert (sampleJson[0].keys() == hc.isAllJsonSpecificSixKeys(result))

            assert(True == hc.isAllJsonFormateAreCorrect_1_and_2(result) )



def test_restCall_2_3():
    baseUrl = "54.191.230.109:443"
    apiName = "threatfeed"

    doubtFull__Apis = ["blocklistde80", "blocklistde993", "blocklistdeapache", "blocklistde443"]

    hc = helperClasses.HelperClasses2()

    for typeAPI in doubtFull__Apis:

        result = api2_toGetArrayOfJsonObjectsOfSpecificType.restCall_2(baseUrl, apiName, typeAPI)
        if result:

            assert (typeAPI == result[0]["type"])

            assert (sampleJson[0].keys() == hc.isAllJsonSpecificSixKeys(result))

            assert(True == hc.isAllJsonFormateAreCorrect_1_and_2(result) )



def test_restCall_2_3():
    baseUrl = "54.191.230.109:443"
    apiName = "threatfeed"

    negativeTestCases = ["randomName", -1, 0, 'a', '$', 'a1', [1, 2]]

    hc = helperClasses.HelperClasses2()

    for typeAPI in negativeTestCases:

        result = api2_toGetArrayOfJsonObjectsOfSpecificType.restCall_2(baseUrl, apiName, typeAPI)
        if result:

            assert (typeAPI == result[0]["type"])

            assert (sampleJson[0].keys() == hc.isAllJsonSpecificSixKeys(result))

            assert(True == hc.isAllJsonFormateAreCorrect_1_and_2(result) )

