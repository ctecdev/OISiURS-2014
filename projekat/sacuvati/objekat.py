'''
Created on 26.06.2014.

@author: Srky
'''
from projekat.osnovno.kompanija import Kompanija

def sacuvatiObjekte(objekti):
    file=open("objekti.txt", "w")
    
    for objekat in objekti:
        for objekat in objekti.children:
            file.write(objekat.idOznakaObj)
            file.write(objekat.naziv)
            file.write(objekat.adresa)
            file.write(objekat.mesto)
            file.write(objekat.opis)
            
            file.write(Kompanija.naziv)#da li treba sacuvati neki atribut kompanije?
            
            file.write("\n")
    file.close()