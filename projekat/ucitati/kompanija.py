'''
Created on 08.06.2014.

@author: Srky
'''

from projekat.vrednosti import Vrednosti

def ucitatiKompanije():
    file=open("kompanije.txt", "r")
    for line in file.readlines():
        values=line.split("|")
        naziv=values[0]
        adresa=values[1]
        mesto=values[2]

        kompanija=(naziv,adresa,mesto)
        Vrednosti.kompanija.children.append(kompanija)
    file.close()