import http.client
import json


def restCall_3_getFirstNameOfAllUsers(baseUrl, apiNameToGetAllUsers):
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



def restCall_6(baseUrl, apiName, userName, payload):
    """

    :param baseUrl:
    :param apiName:
    :param userName:
    :param payload:
    :return:
    """
    conn = http.client.HTTPConnection(baseUrl)

    headers = {
        'cache-control': "no-cache",
        'postman-token': "d8800197-12ea-484f-b84a-34f646cef132"
    }

    pathParameter = "/" + apiName +"/" + userName
    conn.request("DELETE", pathParameter, payload, headers)

    res = conn.getresponse()

    return res.status

