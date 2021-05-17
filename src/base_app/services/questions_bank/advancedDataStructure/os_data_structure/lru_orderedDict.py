# LRU:


# [ 1,2,3,4,5,6,7,8,9,10]

# 11
# [2,3,4,5,6,7,8,9,10, 11]

# 3
# [2,4,5,6,7,8,9,10, 11, 3]
# lru = list()

# def fetch(x):
#     if x in lru:
#         i = indexOf(x)
#         lru.pop(i)
#         lru.append(x)
#         return x



from collections import OrderedDict

class LRUCache:

    def __init__(self):
        self.cache = OrderedDict()
        self.size = 2

    def fetch(self, key):
        if key not in self.cache:
            print("this is a miss, we have to get the work done"
              + "without the cache and get the response stored in the cache for next reference")
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    
    def put(self, key, val):
        self.cache[key] = val
        self.cache.move_to_end(key)
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)

c1 = LRUCache()
print("cache.cache : ", c1.cache)
c1.put(1,1)
print("cache.cache : ", c1.cache)
c1.put(2,2)
print("cache.cache : ", c1.cache)
print(c1.fetch(1))
print("cache.cache : ", c1.cache)
c1.put(3,3)
print("cache.cache : ", c1.cache)
print(c1.fetch(2))
print("cache.cache : ", c1.cache)
c1.put(4,4)
print("cache.cache : ", c1.cache)
print(c1.fetch(1))
print("cache.cache : ", c1.cache)
print(c1.fetch(3))
print("cache.cache : ", c1.cache)
print(c1.fetch(4))

