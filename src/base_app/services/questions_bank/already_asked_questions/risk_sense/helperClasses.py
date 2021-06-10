import datetime


class HelperClasses1(object):
    
    sampleJson = [{
                    "type": "blindferret",
                    "description": "Project Blindferret zmap scanners",
                    "name": "Blindferret",
                    "lastupdate": "2018-12-05 09:24:19",
                    "datatype": "is_ipv4",
                    "frequency": "0"
                }]


    def isAllJsonSpecificSixKeys(self,result):
        for childJson in result:
            if childJson:
                if self.sampleJson[0].keys() != childJson.keys():
                    return False
        else:
            return childJson.keys()


    def isTypeFormateCorrect(self, childJson):
        if childJson:
            typeData = childJson["type"]
            return typeData.isalnum()

        else:
            return False



    def isDescriptionFormateCorrect(self, childJson):
        if childJson:
            descriptionData = childJson["description"]
            return isinstance(descriptionData, str)

        else:
            return False




    def isNameFormateCorrect(self, childJson):
        if childJson:
            nameData = childJson["name"]
            return isinstance(nameData, str)

        else:
            return False



    def isLastUpdateFormateCorrect(self,childJson):
        if childJson:
            timeData =childJson["lastupdate"]

            date_time_obj = datetime.datetime.strptime(timeData, '%Y-%m-%d %H:%M:%S')
            return  isinstance(date_time_obj, datetime.datetime)

        return False

    # "datatype": "is_ipv4",
    def isDataTypeFormateCorrect(self, childJson):
        if childJson:
            return childJson["datatype"] == "is_ipv4"
        return False

    def isfrequencyFormateCorrect(self,childJson):
        if childJson:
            return  childJson["frequency"].isdigit()
        else:
            return False
        

    def isAllJsonFormateAreCorrect_1_and_2(self,result):

        for childJson in result:

            if self.isTypeFormateCorrect(childJson) == False:
                return False
            if self.isDescriptionFormateCorrect(childJson) == False:
                return False
            if self.isNameFormateCorrect(childJson) == False:
                return False
            if self.isLastUpdateFormateCorrect(childJson) == False:
                return False
            if self.isDataTypeFormateCorrect(childJson) == False:
                return False
            if self.isfrequencyFormateCorrect(childJson) == False:
                return False

        return True



class HelperClasses2(HelperClasses1): 
    def isthreatfeedTypeDataCorrect(self,childJson,typeAPI):
        if childJson:
            return  childJson["type"] == typeAPI

        else:
            return False    
        
        
