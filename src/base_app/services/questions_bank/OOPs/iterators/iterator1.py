class Planets(object):
    def __init__(self):
        self._planets = []
        self.index = -1

    def add(self, name):
        self._planets.append(name)

    def __next__(self):
        self.index += 1
        if self.index >= len(self._planets):
            raise StopIteration
        else:
            return self._planets[self.index]

    def __iter__(self):
        return self

arr = ['a', 'b', 'c', 'd']

import copy
arr_copy = arr[:]

arr_copy = arr.copy()

arr_copy = copy.copy(arr)
arr_copy = copy.deepcopy(arr)
arr_copy = arr
print(arr_copy)

Plan = Planets()
Plan.add('earth')
Plan.add('moon')
Plan.add('jupiter')
for planet in Plan:
    print(planet)


# (False or 1) or print('success')
(False or 1) and print('success')

print(complex(3,2) / 2.3)
print(0 / 10 + .1)
# print(10 / 0 + .1)