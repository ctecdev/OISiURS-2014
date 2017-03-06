from dlist import DoubleList

class Set:
    def __init__(self):
        self._list = DoubleList()
    def contains(self, data):
        return self._list.exists(data)
    def insert(self, data):
        if not self._list.exists(data):
            self._list.insert(data)
    def remove(self, data):
        self._list.remove(data)
    def clear(self):
        self._list.clear()
    def values(self):
        return self._list.values()
        
if __name__ == '__main__':
    s = Set()
    s.insert(1)
    s.insert(2)
    s.insert(3)
    s.insert(4)
    s.insert(2)
    s.insert(3)
    print(s.values())
    s.remove(3)
    print(s.values())
    s.remove(2)
    print(s.values())
    