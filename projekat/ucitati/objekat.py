'''
Created on 29.06.2014.

@author: Srky
'''
from projekat.vrednosti import Vrednosti

def ucitatiObjekat():
    file=open("objekti.txt", "r")
    for line in file.readlines():
        values=line.split("|")
        idOznakaObj=values[0]
        naziv=values[1]
        adresa=values[2]
        mesto=values[3]
        opis=values[4]
        
        objekat=(idOznakaObj,naziv,adresa,mesto,opis)
        Vrednosti.kompanija.children.append(objekat)
    file.close()