'''
Created on 29.06.2014.

@author: Srky
'''

from projekat.osnovno.predmet import Predmet
from projekat.vrednosti import pronadjiProstoriju

def ucitajPredmete():
    
    file=open("predmeti.txt","r")
    
    for line in file.readlines():
        values=line.split("|")
        idOznakaPred=values[0]
        naziv=values[1]
        opis=values[2]
        sirina=float(values[3])
        duzina=float(values[4])
        idOznaka=values[5]
        
        prostorija=pronadjiProstoriju(idOznaka)
        predmet=Predmet(idOznakaPred,naziv,opis,sirina,duzina)
        prostorija.children.append(predmet)
        
    file.close()