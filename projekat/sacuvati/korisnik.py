'''
Created on 11.06.2014.

@author: Srky
'''

def sacuvatiKorisnike(korisnici):
    file=open("korisnici.txt", "w")
    
    for korisnik in korisnici:
        for korisnik in korisnici.children:
            file.write(korisnik.idOznakaObj)
            file.write(korisnik.naziv)
            file.write(korisnik.adresa)
            file.write(korisnik.mesto)
            file.write(korisnik.opis)
                        
            file.write("\n")
    file.close()