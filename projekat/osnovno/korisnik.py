'''
Created on 11.06.2014.

@author: Srky
'''

class Korisnik(object):
    '''
    classdocs
    '''


    def __init__(self, identifikacioniKod, ime, prezime):
        '''
        Constructor
        '''
        self.identifikacioniKod=identifikacioniKod
        self.ime=ime
        self.prezime=prezime
        
    def __str__(self):
        return self.identifikacioniKod+" "+self.ime+" "+self.prezime