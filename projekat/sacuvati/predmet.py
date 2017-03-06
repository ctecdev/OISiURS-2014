'''
Created on 26.06.2014.

@author: Srky
'''

def sacuvatiPredmet(kompanije):

    file=open("predmeti.txt", "w")
    
    for kompanija in kompanije:
        for objekat in kompanija.children:
            for prostorija in objekat.children:
                for predmet in prostorija.children:
                    file.write(predmet.idOznakaPred)
                    file.write(predmet.sirina)
                    file.write(predmet.opis)
                    file.write(str(predmet.sirina))
                    file.write(str(predmet.duzina))
                    file.write(predmet.idKodPotrazitelja)
                    file.write(str(predmet.datumPostPredmeta))
                    
                    
                    file.write(prostorija.idOznaka)
                    
                    file.write("\n")