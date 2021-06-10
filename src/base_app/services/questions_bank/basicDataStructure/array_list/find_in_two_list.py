
list1 = list1_SF_dataproc
list2 = list1_SF_airflow

# list1 = list2_Oracle_dataproc
# list2 = list2_Oracle_airflow


for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] not in list2:
            print(list1[i] , "in dataproc but not in airflow")
            break

print("Done")
