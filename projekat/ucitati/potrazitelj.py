'''
Created on May 27, 2014

@author: Srky
'''
from projekat.osnovno.potrazitelj import Potrazitelj
from projekat.vrednosti import Vrednosti

def ucitatiPotrazitelja():
    
    file=open("potrazitelji.txt","r")
    
    for line in file.readlines():
        values=line.split("|")
        identifikacioniKod=values[0]
        ime=values[1]
        prezime=values[2]
        brojTelefona=values[3]
        email=values[4]
        
        korisnik=Potrazitelj(identifikacioniKod,ime,prezime,brojTelefona,email)
        Vrednosti.korisnici.append(korisnik)
        
    file.close()