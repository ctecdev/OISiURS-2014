'''
Created on Jun 10, 2014

@author: Srky
'''
from datetime import datetime
from projekat.vrednosti import Vrednosti, pronadjiKorisnik
from projekat.osnovno.zahtev import Zahtev

def ucitajZahtev():
    try:
        fajl = open("zahtev.txt","r")
        
        for line in fajl.readlines():
            values=line.split("|")
            identifikacioniKod=values[0]
            datum=datetime.strptime(values[1],"%d.%m.%Y %H:%M:%S")
            identifikacioniKodKorinsika=values[2]
            
            korisnik= pronadjiKorisnik(identifikacioniKodKorinsika)
            zahtev=Zahtev(identifikacioniKod, datum, korisnik)
            Vrednosti.zahtevi.append(zahtev)
        
        fajl.close()
    except Exception:
        pass