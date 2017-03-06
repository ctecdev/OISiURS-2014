'''
Created on 29.06.2014.

@author: Srky
'''
from projekat.osnovno.prostorija import Prostorija
from projekat.vrednosti import pronadjiObjekat

def ucitatiProstorije():
    file=open("prostorije.txt", "r")
    
    for line in file.readlines():
        values=line.split("|")
        idOznaka=values[0]
        sirina=float(values[1])
        duzina=float(values[2])
        idOznakaObj=values[3]
        objekat=pronadjiObjekat(idOznakaObj)
        
        prostorija=Prostorija(idOznaka,sirina,duzina)
        objekat.children.append(prostorija)
    file.close()