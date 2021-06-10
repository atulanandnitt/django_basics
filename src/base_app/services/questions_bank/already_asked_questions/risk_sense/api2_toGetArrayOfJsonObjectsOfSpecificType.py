#2. /threatfeed/{threatfeed-type} [ GET ]

import http.client
import json


def restCall_2(baseUrl, apiName, typeAPI):

    conn = http.client.HTTPConnection(baseUrl)
    pathParameter = "/" + apiName + "/" + typeAPI
    headers = {
        'cache-control': "no-cache",
        'postman-token': "e4d3f8ab-37de-acd4-a06d-2608f0423068"
    }

    conn.request("GET", pathParameter, headers=headers)

    res = conn.getresponse()
    json_object_list = json.load(res)


    return json_object_list

