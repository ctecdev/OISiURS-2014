'''
Created on May 13, 2014

@author: zek
'''
from projekat.osnovno.kompanija import Kompanija
from projekat.osnovno.predmet import Predmet


class Vrednosti(object):
    '''
    classdocs
    '''
    kompanija=Kompanija("Komapnija1", "Adresa1", "Mesto1")
    treeIndentation="       "
    korisnici=[]
    menadzer="Menadzer"
    radnik="Radnik"
    zahtevi=[]

def preorderTraversalChanged(subtree,indentation):
    if subtree is not None:
        print(indentation+str(subtree))
        if type(subtree) is Predmet:
            return
        for node in subtree.children:
            preorderTraversalChanged(node,indentation+Vrednosti.treeIndentation)

def pronadjiObjekat(idOznakaObj):
    for objekat in Vrednosti.kompanija.children:
        if objekat.idOznakaObj ==idOznakaObj:
            return objekat
    
    return None   

def pronadjiProstoriju(idOznaka):
    for objekat in Vrednosti.kompanija.children:
        for prostorija in objekat.children:
            if prostorija.idOznaka==idOznaka:
                return prostorija
    return None     

def pronadjiKorisnik(identifikacioniKod):
    for korisnik in Vrednosti.korisnici:
        if korisnik.identifikacioniKod==identifikacioniKod:
            return korisnik
    return None