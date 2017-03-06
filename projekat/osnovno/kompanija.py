'''
Created on 08.06.2014.

@author: Srky
'''
from tree import TreeParentNode

class Kompanija(TreeParentNode):
    '''
    classdocs
    '''


    def __init__(self, naziv, adresa, mesto):
        '''
        Constructor
        '''
        TreeParentNode.__init__(self)
        self.naziv=naziv
        self.adresa=adresa
        self.mesto=mesto
        
    def __str__(self):
        return self.naziv+" "+self.adresa+" "+self.mesto