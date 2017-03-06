'''
Created on 26.06.2014.

@author: Srky
'''

def sacuvatiZahtev(zahtevi):
    file=open("zahtevi.txt", "w")
    
    for zahtev in zahtevi:
        file.write(zahtev.idKod)
        file.write(str(zahtev.datumZahteva))
        file.write(zahtev.tipZahteva)
        file.write(zahtev.statusZahteva)
        file.write(zahtev.idKodMenPot)
        
        file.write("\n")
    file.close()