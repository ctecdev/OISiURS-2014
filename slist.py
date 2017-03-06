class SingleList:
    """
    Jednostruko spregnuta lista.
    """
    def __init__(self):
        """
        Inicijalizacija liste: lista je na pocetku prazna. To se oznacava tako
        sto referenca na prvi element liste (self.head) ima vrednost None.
        """
        self.head = None
    
    def insert(self, data):
        """
        Ubacivanje novog elementa u listu, na njen pocetak. Podatak koji se
        upisuje dat je parametrom data.
        """
        newNode = _SingleListNode(data)
        newNode.next = self.head
        self.head = newNode
        
    def append(self, data):
        """
        Dodavanje novog elementa na kraj liste. Podatak koji se upisuje dat je
        parametrom data.
        """
        newNode = _SingleListNode(data)
        if self.head is None:
            self.head = newNode
            return
        curNode = self.head
        while curNode.next is not None:
            curNode = curNode.next
        curNode.next = newNode
        
    def exists(self, data):
        """
        Trazenje datog podatka u listi. Funkcija vraca True ako je podatak 
        pronadjen, inace vraca False. Trazeni podatak dat je parametrom data.
        """
        curNode = self.head
        while curNode is not None and curNode.data != data:
            curNode = curNode.next
        return curNode is not None
        
    def remove(self, data):
        """
        Uklanja prvi nadjeni element sa vrednoscu data iz liste.
        """
        # ako je lista prazna, ne radi nista
        if self.head is None:
            return
        # ako treba izbaciti prvi element, samo pomeri head na sledeci u listi
        # ako lista ima jedan element, head ce biti None
        if self.head.data == data:
            self.head = self.head.next
            return
        # ako se ne izbacuje prvi element, u petlji ga trazimo medju narednim
        # elementima
        curNode = self.head
        while curNode.next is not None and curNode.next.data != data:
            curNode = curNode.next
        if curNode.next is not None:
            curNode.next = curNode.next.next
        
    def removeIndex(self, i):
        """
        Uklanja i-ti element iz liste.
        """
        if self.head is None:
            return
        if i == 0:
            self.head = self.head.next
            return
        curNode = self.head
        pos = 1
        while curNode.next is not None and pos < i-1:
            curNode = curNode.next
            pos = pos + 1
        if curNode.next is not None:
            curNode.next = curNode.next.next
        
    def values(self):
        """
        Vraca sadrzaj liste u obliku klasicne Python liste
        """
        retVal = []
        curNode = self.head
        while curNode is not None:
            retVal.append(curNode.data)
            curNode = curNode.next
        return retVal
    
    def index(self, i):
        """
        Vraca podatak iz liste koji se nalazi na i-toj poziciji. Pozicije
        se broje od 0. Ako lista ima manje od i+1 elemenata, vraca None.
        """
        # moramo ici sekvencijalno kroz listu dok ne dodjemo do i-tog elementa
        curNode = self.head
        # trebace nam brojac pozicija u listi
        pos = 0
        while curNode is not None and pos < i:
            curNode = curNode.next
            pos = pos + 1
        if curNode is None:
            return None
        else:
            return curNode.data
    
    def size(self):
        """
        Vraca broj elemenata liste.
        """
        count = 0
        curNode = self.head
        while curNode is not None:
            curNode = curNode.next
            count = count + 1
        return count

    def clear(self):
        """
        Uklanja sve elemente iz liste.
        """
        self.head = None
    
# Element jednostruko spregnute liste
class _SingleListNode:
    """
    Element jednostruko spregnute liste. Ima dva atributa: data cuva podatak
    koji predstavlja element liste; next cuva referencu na sledeci element
    liste (sledeci element liste je takodje tipa _SingleListNode).
    """
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == '__main__':
    # napravimo jednostruko spregnutu listu; inicijalno je prazna
    slist = SingleList()
    # dodajemo elemente na njen kraj
    slist.append(1)
    slist.append(2)
    slist.append(3)
    slist.append(4)
    slist.append(5)
    slist.append(6)
    # sada bi u listi trebalo da ima 6 elemenata, sa vrednostima 1,2,3,4,5,6
    print(slist.size())
    print(slist.values())
    # uklonimo broj 7 iz liste (takvog nema)
    slist.remove(7)
    # sada bi sadrzaj liste trebalo da bude nepromenjen
    print(slist.values())
    # uklonimo broj 6 iz liste (poslednji)
    slist.remove(6)
    # sada bi lista trebalo da glasi 1,2,3,4,5
    print(slist.values())
    # uklonimo broj 1 iz liste (prvi)
    slist.remove(1)
    # sada bi lista trebalo da glasi 2,3,4,5
    print(slist.values())
    # uklonimo broj 3 iz liste (iz sredine)
    slist.remove(3)
    # sada bi lista trebalo da glasi 2,4,5
    print(slist.values())
    # da proveravamo da li u listi postoji broj 4
    print(slist.search(4))
    # vrati element sa indeksom 1 (trebalo bi dobiti 4)
    print(slist.index(1))
    # vrati element sa indeksom 53 (trebalo bi dobiti None)
    print(slist.index(53))