import http.client
import json
#from helperClasses import HelperClasses1
import pytest


def restCall_1(baseUrl, apiName, n):
    conn = http.client.HTTPConnection(baseUrl)

    headers = {
        'cache-control': "no-cache",
        'postman-token': "ed0b6cc7-f185-4f9a-d1c2-839beac55b5d"
    }
    pathParameter = "/" + apiName
    queryParameter = "limit=" + str(n)
    resourcePath = pathParameter + "?" + queryParameter
    conn.request("GET", resourcePath, headers=headers)

    res = conn.getresponse()
    json_object_list = list()
    if res:
        json_object_list = json.load(res)

    return json_object_list

