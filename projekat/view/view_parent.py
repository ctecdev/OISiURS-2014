'''
Created on May 6, 2014

@author: zek
'''

class View(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.praznaMesta="                 "
    
    
    def emptyBegin(self):
        for i in range(10):
            print
    
    def ispis(self,tekst):
        print self.praznaMesta+tekst
    def unos(self, tekst):
        return raw_input(self.praznaMesta+tekst)
    
    def showView(self):
        self.emptyBegin()
        self.showChild()
        
    def showChild(self):
        pass