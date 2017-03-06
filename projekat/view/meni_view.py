'''
Created on May 6, 2014

@author: zek
'''
from projekat.view.view_parent import View
from projekat.view.ispis.ispis_poruka import PorukaView

class MeniView(View):
    '''
    classdocs
    '''
    
    def __init__(self):
        View.__init__(self)
    
    def showView(self):
        while True:
            self.emptyBegin()
            self.ispis("Opcije")
            self.ispis("1 - Opcija 1")
            self.ispis("2 - Opcija 2")
            self.ispis("x - Izlaz")
            opcija=self.unos("Izaberite opciju:")
            
            if opcija=="1":
                pass
            elif opcija=="2":
                pass
            elif opcija=="x":
                return 
            else:
                view=PorukaView("Opcija koju ste uneli ne postoji")
                view.showView()