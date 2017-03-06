'''
Created on May 6, 2014

@author: zek
'''
from projekat.view.view_parent import View


class PorukaView(View):
    '''
    classdocs
    '''


    def __init__(self, poruka):
        '''
        Constructor
        '''
        View.__init__(self)
        self.poruka=poruka
        
    def showChild(self):
        self.ispis(self.poruka)
        self.unos("Unesite Enter za dalje...")