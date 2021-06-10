import http.client
import json


def restCall_7(baseUrl, apiName, userName, payload):

    conn = http.client.HTTPConnection(baseUrl)

    headers = {
        'cache-control': "no-cache",
        'postman-token': "d8800197-12ea-484f-b84a-34f646cef132"
    }

    pathParameter = "/" + apiName +"/" + userName
    conn.request("PUT", pathParameter, payload, headers)

    res = conn.getresponse()

    return res.status