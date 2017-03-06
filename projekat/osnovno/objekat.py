'''
Created on 08.06.2014.

@author: Srky
'''
from tree import TreeParentNode

class Objekat(TreeParentNode):
    '''
    classdocs
    '''


    def __init__(self, idOznakaObj, naziv, adresa, mesto, opis):
        '''
        Constructor
        '''
        TreeParentNode.__init__(self)
        self.idOznakaObj=idOznakaObj
        self.naziv=naziv
        self.adresa=adresa
        self.mesto=mesto
        self.opis=opis
    def __str__(self):
        return self.idOznakaObj+" "+self.naziv+" "+self.adresa+" "+self.mesto+" "+self.opis