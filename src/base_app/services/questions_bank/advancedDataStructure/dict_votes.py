

def winner(listNames):
    set1=set(listNames)
    print("set1",set1)
    result_dict = dict( [ (key, listNames.count(key)) for key in set1 ] )
    print(result_dict,type(result_dict))
    print("all max key val")
    allKeys=[key2 for key2,values2 in result_dict.items() ]
    print("allKeys",allKeys)
    
    allKeywithMaxVal=[key2 for key2,values2 in result_dict.items() if values2 == max(result_dict.values())]
    #allKeywithMaxVal=[val for key,val in result_dict.items() if val == max(result_dict.values())]
    print("allKeywithMaxVal",allKeywithMaxVal)
    #solString= ','.join(sorted(allKey))
    #print(solString,type(solString))
    allKeywithMaxVal.sort()#solString.split(',')
    print("allKeywithMaxVal",allKeywithMaxVal,type(allKeywithMaxVal))
    #allSortedKey=sorted(allKeywithMaxVal)
    #print(allSortedKey,type(allSortedKey))
    sol=allKeywithMaxVal.pop()#will by default take last element   #sol=allKey.pop(0)
    print(sol)

list1=['apple','red','apple','red','red','pear','rid','rid','rid','rad','rad','rad']    
list1=['a','b','c','a','b','a','b']
winner(list1)
#print(set(winner))
 