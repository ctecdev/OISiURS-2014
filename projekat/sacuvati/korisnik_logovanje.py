'''
Created on May 27, 2014

@author: zek
'''
from projekat.osnovno.korisnik_logovanje import KorisnikLogovanje

def sacuvatiKorisnikLogovanje(korisnici):
    
    fajl=open("korisnik_logovanje.txt","w")
    
    for korisnik in korisnici:
        if type(korisnik) is KorisnikLogovanje:        
            fajl.write(korisnik.identifikacioniKod+"|")
            fajl.write(korisnik.ime+"|")
            fajl.write(korisnik.prezime+"|")
            fajl.write(korisnik.korisnickoIme+"|")
            fajl.write(korisnik.lozinka+"|")
            fajl.write(korisnik.tipKorisnika+"|")
             
            fajl.write("\n")
    
    fajl.close()