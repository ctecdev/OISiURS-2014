'''
Created on May 27, 2014

@author: Srky
'''
from projekat.osnovno.potrazitelj import Potrazitelj

def sacuvatiPotrazitelja(korisnici):
    
    fajl=open("potrazitelji.txt","w")
    
    for korisnik in korisnici:
        if type(korisnik) is Potrazitelj:        
            fajl.write(korisnik.identifikacioniKod+"|")
            fajl.write(korisnik.ime+"|")
            fajl.write(korisnik.prezime+"|")
            fajl.write(korisnik.brojTelefona+"|")
            fajl.write(korisnik.email+"|")
             
            fajl.write("\n")
    
    fajl.close()