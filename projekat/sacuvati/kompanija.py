'''
Created on 08.06.2014.

@author: Srky
'''

def sacuvatiKompanije(kompanije):
    file=open("kompanije.txt", "w")
    
    for kompanija in kompanije:
        for kompanija in kompanije.children:
            file.write(kompanija.naziv)
            file.write(kompanija.adresa)
            file.write(kompanija.mesto)
            
            file.write("\n")
    file.close()