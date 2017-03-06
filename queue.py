from dlist import DoubleList

class Queue:
    """
    Implementacija reda (queue).
    """
    def __init__(self):
        """
        Inicijalizacija reda: red je prazan. Atribut u kome cuvamo 
        podatke bice dvostruko spregnuta lista.
        """
        self._list = DoubleList()

    def values(self):
        """
        Vraca sadrzaj reda u obliku klasicne Python liste.
        """
        return self._list.values()

    def clear(self):
        """
        Uklanja sve elemente iz reda.
        """
        self._list.clear()
    
    def enqueue(self, data):
        """
        Dodaje element u red.
        """
        self._list.insert(data)
        
    def dequeue(self):
        """
        Uklanja element iz reda i vraca njegovu vrednost. Ako je red
        prazan, vraca None.
        """
        size = self._list.size()
        if size == 0:
            return None
        data = self._list.tail.data
        self._list.removeIndex(size-1)
        return data

if __name__ == '__main__':
    red = Queue()
    red.enqueue(1)
    red.enqueue(2)
    red.enqueue(3)
    print(red.values())
    value = red.dequeue()
    print("Dequeued:", value)
    value = red.dequeue()
    print("Dequeued:", value)
    value = red.dequeue()
    print("Dequeued:", value)
