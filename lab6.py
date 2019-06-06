import random
import time 
import matplotlib.pyplot as plt

class HashTable():
    
    bucket_size = 5
    minimum_buckets = 3

    def __init__(self, capacity = bucket_size * minimum_buckets):
        self.size = 0
        self.threshold = capacity
        self.buckets = [[] for i in range(capacity // self.bucket_size)]      

    def insert(self, element):
        print("key = ", element.key,"size = ", self.size, 'len = ', len(self.buckets))
        ind = self.hash(element.key)
        for el in (self.buckets[ind]):
            if el.key == element.key:
                el.setValue(element.value)
                return
        else:
            self.buckets[ind].append(element)
            self.size += 1
            if self.size == self.threshold:
                self.resize()

    def resize(self):
        self.threshold *= 2
        self.minimum_buckets *= 2
        old = self.buckets        
        self.buckets = [[] for i in range(self.threshold // self.bucket_size)]
        for buc in old:
            for el in buc:
                new_ind = self.hash(el.key)
                self.buckets[new_ind].append(el)

    def get(self, key):
        ind = self.hash(key)
        for el in self.buckets[ind]:
            if el.key == key:
                print("Значение ", key, ' = ', el.value)
                return el.value
        print("No such key")

    def erase(self, key):
        ind = self.hash(key)
        for el in self.buckets[ind]:
            if el.key == key:
                del el
                self.size -= 1
                print(key, ' is deleted')
                return
        print("No such key")     

    def show(self):
        ind = 0
        for bucket in self.buckets:
            print(ind, '//', bucket)
            ind += 1
            print()

    def __len__(self):
        return self.size

    def hash(self, key):
        return hash(key) % len(self.buckets)
    

class Element():

    def __init__(self, _key, _value):
        self.key = _key
        self.value = _value

    def __repr__(self):
        return str(self.key) + " : " + self.value

    def setValue(self, val):
        self.value = val

table = HashTable(100)
dict = {}
t_moy, t_stand = [], []
kol = [x for x in range(10, 40, 1)]

for i in range(30):
    t1 = time.time()
    for size in range(10, 20, 1):
        key = random.randint(size, size + 1)
        # добавление в мою хэш-таблицу
        table.insert(Element(key, str(key)))        
    t_moy.append(time.time() - t1)

for i in range(30):
    t1 = time.time()
    for size in range(10, 20, 1):
        key = random.randint(size, size + 1)
        # добавление в стандартную хэш-таблицу
        dict[key] = str(key)
    t_stand.append(time.time() - t1)

plt.plot(kol, t_moy, 'r-', linewidth=1, label = 'My hashtable')
plt.plot(kol, t_stand, 'b-', linewidth=1, label = 'Standart hashtable')
plt.title("Hash-table")
plt.xlabel('kol')
plt.ylabel('t')
plt.grid(True)
plt.legend(loc = 0)
plt.show()













# dict = {}
# dict[4] = '4'
# dict[5] = '5'
# dict[6] = '6'
# print(dict)































