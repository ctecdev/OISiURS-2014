'''
Created on May 27, 2014

@author: zek
'''
from projekat.osnovno.korisnik_logovanje import KorisnikLogovanje
from projekat.vrednosti import Vrednosti

def ucitatiKorisnikLogovanje():
    
    file=open("korisnik_logovanje.txt","r")
    
    for line in file.readlines():
        values=line.split("|")
        identifikacioniKod=values[0]
        ime=values[1]
        prezime=values[2]
        korisnickoIme=values[3]
        lozinka=values[4]
        tipKorisnika=values[5]
        
        korisnik=KorisnikLogovanje(identifikacioniKod,ime,prezime,korisnickoIme,lozinka,tipKorisnika)
        Vrednosti.korisnici.append(korisnik)
        
    file.close()