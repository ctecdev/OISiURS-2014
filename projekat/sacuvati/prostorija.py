'''
Created on 26.06.2014.

@author: Srky
'''

def sacuvatiProstorije(kompanije):
    file=open("prostorije.txt", "w")
    
    for kompanija in kompanije:
        for objekat in kompanija.children:
            for prostorija in objekat.children:
                file.write(prostorija.idOznaka)
                file.write(str(prostorija.sirina))
                file.write(str(prostorija.duzina))
                
                file.write(objekat.idOznakaObj)
                
                file.write("\n")
    file.close()