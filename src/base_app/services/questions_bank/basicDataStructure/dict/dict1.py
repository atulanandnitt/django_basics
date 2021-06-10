dict1={'A':['11'], 'B':['22'], 'C':['33']}
print(dict1)

dict1['A'].append(12)
print(dict1)

val = '44'
list_val = list()
list_val.append(val)
try:
    dict1['D'].append(list_val)
except KeyError:
    dict1['D']= list_val
print(dict1)

val2 = '55'
list_val2 = list()
list_val2.append(val2)
try:
    dict1['D'].append(val2)
except KeyError:
    dict1['D']= list_val2
print(dict1)
