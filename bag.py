from dlist import DoubleList

class Bag:
    def __init__(self):
        self._list = DoubleList()
    def contains(self, data):
        return self._list.exists(data)
    def insert(self, data):
        self._list.insert(data)
    def remove(self, data):
        self._list.remove(data)
    def clear(self):
        self._list.clear()
    def values(self):
        return self._list.values()

if __name__ == '__main__':
    b = Bag()
    b.insert(1)
    b.insert(2)
    b.insert(3)
    b.insert(4)
    b.insert(2)
    b.insert(3)
    print(b.values())
    b.remove(3)
    print(b.values())
    b.remove(2)
    print(b.values())
    b.remove(2)
    print(b.values())
