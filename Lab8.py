import time
from random import randrange


class HashTable:
    def __init__(self):
        self.size = 200000
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] is not None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    @staticmethod
    def hashfunction(key, size):
        return key % size

    @staticmethod
    def rehash(oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


HK = HashTable()

start_time = time.time()
for i in range(randrange(0, 1000)):
    HK[i] = randrange(0, 1000)
print("--- 1K elements INSERTED: %s seconds ---" % (time.time() - start_time))
start_time = time.time()
for j in range(randrange(0, 500)):
    for S in range(0, 500):
        S = HK[j]
print("--- 1K elements SEARCHED: %s seconds ---" % (time.time() - start_time))

H100K = HashTable()

start_time = time.time()
for i in range(randrange(0, 10000)):
    H100K[i] = randrange(0, 10000)
print("--- 10K elements INSERTED: %s seconds ---" % (time.time() - start_time))
start_time = time.time()
for j in range(randrange(0, 500)):
    for S in range(0, 500):
        S = H100K[j]
print("--- 10K elements SEARCHED: %s seconds ---" % (time.time() - start_time))

H100K = HashTable()

start_time = time.time()
for i in range(randrange(0, 100000)):
    H100K[i] = randrange(0, 100000)
print("--- 100K elements INSERTED: %s seconds ---" % (time.time() - start_time))
start_time = time.time()
for j in range(randrange(0, 500)):
    for S in range(0, 500):
        S = H100K[j]
print("--- 100K elements SEARCHED: %s seconds ---" % (time.time() - start_time))

H200K = HashTable()

start_time = time.time()
for i in range(randrange(0, 200000)):
    H200K[i] = randrange(0, 200000)
print("--- 200K elements INSERTED: %s seconds ---" % (time.time() - start_time))
start_time = time.time()
for j in range(randrange(0, 500)):
    for S in range(0, 500):
        S = H200K[j]
print("--- 200K elements SEARCHED: %s seconds ---" % (time.time() - start_time))
