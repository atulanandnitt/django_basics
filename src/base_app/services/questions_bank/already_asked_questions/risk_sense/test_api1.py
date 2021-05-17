import pytest
from . import api1_toGetArrayOfJsonObjects
from . import helperClasses




sampleJson = [{
    "type": "blindferret",
    "description": "Project Blindferret zmap scanners",
    "name": "Blindferret",
    "lastupdate": "2018-12-05 09:24:19",
    "datatype": "is_ipv4",
    "frequency": "0"
}]



def test_restCall_1_1(n=1):
    """
    Positive test case of list of size 1
    :param n:
    :return:
    """

    apiName = "threatfeeds"
    baseUrl = "54.191.230.109:443"

    hc = helperClasses.HelperClasses1()

    result = api1_toGetArrayOfJsonObjects.restCall_1(baseUrl, apiName, n)
    if result != []:

        assert (n == len(result))

        assert (sampleJson[0].keys() == hc.isAllJsonSpecificSixKeys(result))

        assert(True == hc.isAllJsonFormateAreCorrect_1_and_2(result) )



def test_restCall_1_2(n=0):
    """
    Positive test case to return Empty list
    :param n:
    :return:
    """

    apiName = "threatfeeds"
    baseUrl = "54.191.230.109:443"

    hc = helperClasses.HelperClasses1()

    result = api1_toGetArrayOfJsonObjects.restCall_1(baseUrl, apiName, n)
    if result != []:

        assert (n == len(result))

        assert (sampleJson[0].keys() == hc.isAllJsonSpecificSixKeys(result))

        assert(True == hc.isAllJsonFormateAreCorrect_1_and_2(result) )



def test_restCall_1_3(n="5.5"):
    """
    Positive test case: take the floor and return list of length int(5.5)
    :param n:
    :return:
    """

    apiName = "threatfeeds"
    baseUrl = "54.191.230.109:443"

    hc = helperClasses.HelperClasses1()

    result = api1_toGetArrayOfJsonObjects.restCall_1(baseUrl, apiName, n)

    assert ( (n//1) == len(result))

    assert (sampleJson[0].keys() != hc.isAllJsonSpecificSixKeys(result))

    assert(True != hc.isAllJsonFormateAreCorrect_1_and_2(result) )


def test_restCall_1_4(n="toFail123@!$#$@"):
    """
    Negative test case
    :param n:
    :return:
    """

    apiName = "threatfeeds"
    baseUrl = "54.191.230.109:443"

    hc = helperClasses.HelperClasses1()

    result = api1_toGetArrayOfJsonObjects.restCall_1(baseUrl, apiName, n)

    assert (n != len(result))

    assert (sampleJson[0].keys() != hc.isAllJsonSpecificSixKeys(result))

    assert(True != hc.isAllJsonFormateAreCorrect_1_and_2(result) )


def test_restCall_1_5(n="randomeNonNumericData"):
    """
    Negative Test case
    :param n:
    :return:
    """

    apiName = "threatfeeds"
    baseUrl = "54.191.230.109:443"

    hc = helperClasses.HelperClasses1()

    result = api1_toGetArrayOfJsonObjects.restCall_1(baseUrl, apiName, n)

    assert (n != len(result))

    assert (sampleJson[0].keys() != hc.isAllJsonSpecificSixKeys(result))

    assert(True != hc.isAllJsonFormateAreCorrect_1_and_2(result) )


def test_restCall_1_6(n="-1"):
    """
    Negative Test case
    :param n:
    :return:
    """

    apiName = "threatfeeds"
    baseUrl = "54.191.230.109:443"

    hc = helperClasses.HelperClasses1()

    result = api1_toGetArrayOfJsonObjects.restCall_1(baseUrl, apiName, n)
    assert (n != len(result))

    assert (sampleJson[0].keys() != hc.isAllJsonSpecificSixKeys(result))

    assert(True != hc.isAllJsonFormateAreCorrect_1_and_2(result) )


def test_restCall_1_7(n="-121"):
    """
    Negative Test case
    :param n:
    :return:
    """

    apiName = "threatfeeds"
    baseUrl = "54.191.230.109:443"

    hc = helperClasses.HelperClasses1()

    result = api1_toGetArrayOfJsonObjects.restCall_1(baseUrl, apiName, n)

    assert (n != len(result))

    assert (sampleJson[0].keys() != hc.isAllJsonSpecificSixKeys(result))

    assert(True != hc.isAllJsonFormateAreCorrect_1_and_2(result) )
