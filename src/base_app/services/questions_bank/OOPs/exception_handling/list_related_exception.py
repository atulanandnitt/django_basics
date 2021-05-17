n=7
occupancy_array = [i for i in range(n)]
print(occupancy_array[3])

if occupancy_array[3]:
    print("something found")
else:
    print("nothing found")

occupancy_array.pop(3)
print(occupancy_array)
occupancy_array.insert(3,None)
print(occupancy_array)

if occupancy_array[3]:
    print("something found")
else:
    print("nothing found")