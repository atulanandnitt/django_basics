import http.client
import json
#from helperClasses import HelperClasses1
import pytest


def restCall_4(baseUrl,apiName,userName):

    # http://54.191.230.109:443/user/Eve
    reqUri = "/"+ apiName + "/" + userName

    conn = http.client.HTTPSConnection(baseUrl)

    headers = {
        'authorization': "OAuth KeyData",
        'cache-control': "no-cache",
        'postman-token': "cce8fe7a-ff04-1c54-85c3-77fb2afdd34e"
    }

    conn.request("GET", reqUri, headers=headers)

    res = conn.getresponse()
    data = res.read()

    jsonData = data.decode("utf-8")

    return jsonData

