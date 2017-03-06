'''
Created on 11.06.2014.

@author: Srky
'''
from projekat.osnovno.korisnik import Korisnik

class KorisnikLogovanje(Korisnik):
    '''
    classdocs
    '''


    def __init__(self, identifikacioniKod, ime, prezime, korisnickoIme, lozinka, tipKorisnika):
        '''
        Constructor
        '''
        Korisnik.__init__(self, identifikacioniKod, ime, prezime)
        self.korisnickoIme=korisnickoIme
        self.lozinka=lozinka
        self.tipKorisnika=tipKorisnika
        
    def __str__(self):
        return self.identifikacioniKod+" "+self.ime+" "+self.prezime+" "+self.korisnickoIme+" "+self.tipKorisnika