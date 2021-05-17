date_time_str = '2018-06-29 08:15:27.243860'
print("date_time_str",date_time_str,type(date_time_str))
date_time_obj = objective_clarifications.summary_notes.advancedDataStructure.string.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

print('Date:', date_time_obj.date())  
print('Time:', date_time_obj.time())  
print('Date-time:', date_time_obj)  


sampleJson2 = [{
            "type": "blindferret",
            "description": "Project Blindferret zmap scanners",
            "name": "Blindferret",
            "lastupdate": "2018-12-05 09:24:19",
            "datatype": "is_ipv4",
            "frequency": "0"
        }]

timeData =sampleJson2[0]["lastupdate"]
print("timeData" , timeData , type(timeData))

date_time_obj = objective_clarifications.summary_notes.advancedDataStructure.string.datetime.strptime(timeData, '%Y-%m-%d %H:%M:%S')

print("date_time_obj",date_time_obj,type(date_time_obj))


import random
print(random.randint(1,11))

random.sample(range(1, 100), 3)



allUserNamesReadFromAPI3 = ['a','b','c','d','e']
noOfTestCases=3
setOfUserNames= set()
print(len(setOfUserNames))
while len(setOfUserNames) < noOfTestCases:
    randomNo = random.randint(1,len(allUserNamesReadFromAPI3))
    print(randomNo)
    setOfUserNames.add(allUserNamesReadFromAPI3[randomNo])
    
print(setOfUserNames)    

for item in setOfUserNames:
    print("item is ",item)