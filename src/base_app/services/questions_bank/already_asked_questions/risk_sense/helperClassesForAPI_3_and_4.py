import datetime
import re


class HelperClassesForAPI_4(object):
    sampleJson = [{
        "id": "121212",
        "first_name": "string",
        "last_name": "string",
        "avatar": "string"
    }]

    def isJsonHasSpecificFourKeys(self, jsonObject):
        if self.sampleJson[0].keys() != childJson.keys():
            return False
        else:
            return True

    def isIdFormateCorrect(self,childJson):
        if childJson:
            return  childJson["id"].isdigit()
        else:
            return False


    def isFirstNameFormateCorrect(self, childJson):
        if childJson:
            nameData = childJson["first_name"]
            return isinstance(nameData, str)

        else:
            return False

    def isLastNameFormateCorrect(self, childJson):
        if childJson:
            nameData = childJson["last_name"]
            return isinstance(nameData, str)

        else:
            return False


    def isAvatarFormateCorrect(self, childJson):
        if childJson:
            nameData = childJson["avatar"]
            return isinstance(nameData, str)

        else:
            return False


    def isAllJsonFormateAreCorrect_3_and_4(self,childJson):

        if self.isIdFormateCorrect(childJson) == False:
            return False
        if self.isFirstNameFormateCorrect(childJson) == False:
            return False
        if self.isLastNameFormateCorrect(childJson) == False:
            return False
        if self.isAvatarFormateCorrect(childJson) == False:
            return False

        else:
            return True


class HelperClassesForAPI_3(HelperClassesForAPI_4):

    def isEachJsonOfTheArrayHasCorrectDataFormate_3(self, result):
        for childJson in result:
            if self.isAllJsonHasCorrectFormatOfValuesCorrospondingToAll4Keys(childJson) == False:
                return False
        return True

    def isEachJsonOfArrayHasSpecificFourKeys_3(self,result):
        for childJson in result:
            if childJson:
                if self.isJsonHasSpecificFourKeys(childJson) == False:
                    return False
        else:
            return True




