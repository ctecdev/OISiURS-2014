'''
Created on 08.06.2014.

@author: Srky
'''

class Predmet(object):
    '''
    classdocs
    '''

    def __init__(self, idOznakaPred, naziv, opis, sirina, duzina, idKodPotrazitelja, datumPostPredmeta):
        '''
        Constructor
        '''
        self.idOznakaPred=idOznakaPred
        self.naziv=naziv
        self.opis=opis
        self.sirina=sirina
        self.duzina=duzina
        self.idKodPotrazitelja=idKodPotrazitelja
        self.datumPostPredmeta=datumPostPredmeta
        
    def __str__(self):
        return self.idOznakaPred+" "+self.naziv+" "+self.opis+" "+str(self.sirina)+" "+str(self.duzina)+" "+self.idKodPotrazitelja+" "+str(self.datumPostPredmeta)