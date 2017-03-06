'''
Created on 08.06.2014.

@author: Srky
'''

class Zahtev(object):
    '''
    classdocs
    '''

    def __init__(self, idKod, datumZahteva, tipZahteva, statusZahteva, idKodMenPot):
        '''
        Constructor
        '''
        self.idKod=idKod
        self.datumZahteva=datumZahteva
        self.tipZahteva=tipZahteva
        self.statusZahteva=statusZahteva
        self.idKodMenPot=idKodMenPot
    def __str__(self):
        return self.idKod+" "+str(self.datumZahteva)+" "+self.tipZahteva+" "+self.statusZahteva+" "+self.idKodMenPot