'''
Created on 08.06.2014.

@author: Srky
'''
from tree import TreeParentNode

class Prostorija(TreeParentNode):
    '''
    classdocs
    '''

    def __init__(self, idOznaka, sirina, duzina):
        '''
        Constructor
        '''
        TreeParentNode.__init__(self)
        self.idOznaka=idOznaka
        self.sirina=sirina
        self.duzina=duzina
        
    def __str__(self):
        return self.idOznaka+" "+str(self.sirina)+" "+str(self.duzina)