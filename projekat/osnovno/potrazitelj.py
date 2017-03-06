'''
Created on 11.06.2014.

@author: Srky
'''
from projekat.osnovno.korisnik import Korisnik

class Potrazitelj(Korisnik):
    '''
    classdocs
    '''

    def __init__(self, identifikacioniKod, ime, prezime, brojTelefona, email):
        '''
        Constructor
        '''
        Korisnik.__init__(self, identifikacioniKod, ime, prezime)
        self.brojTelefona=brojTelefona
        self.email=email
        
    def __str__(self):
        return self.identifikacioniKod+" "+self.ime+" "+self.prezime+" "+self.brojTelefona+" "+self.email