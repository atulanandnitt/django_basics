# 3. /users [ GET

import http.client
import datetime
import json
from . import helperClassesForAPI_3_and_4


def restCall_3(baseUrl, apiName):
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

    return json_object_list


