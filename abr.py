#! /usr/bin/env python
# -*- coding: UTF-8 -*-


##classe arbre binaire de recherche

class ABR:
    ##fonction d'initialisation
    def __init__(self):
        self.val = None ##valeur du noeud - initialiser à vide
        self.sag = None ##sous arbre gauche - initialiser à vide
        self.sad = None ##sous arbre droit - initialiser à vide

    ##fonction qui insère un élément x dans l'arbre binaire de recherche courant
    def insererABR(self, x):
        res = True
        if self.val is None:
            self.val = x
        else:
            if x < self.val:
                if self.sag is None:
                    self.sag = ABR()
                self.sag.insererABR(x)
            elif x > self.val:
                if self.sad is None:
                    self.sad = ABR()
                self.sad.insererABR(x)
            else:
                res = False
        return res

    ##fonction annexe de suppression d'un élément de l'arbre binaire courant
    def supprimerMAX(self):
        if self.sad is None:
            y = self.val
            if self.sag is not None:
                aux = self.sag
                self.sag = None
                self.val = aux.val
        else:
            y = self.sad.supprimerMAX()
            if self.sad.val == y:
                self.sad = None
        return y

    ##focntion de suppression d'un élément x de l'abre binaire de recherche courant
    def supprimerABR(self,x):
        a = False
        if self is not None:
            ## un seul fils à gauche
            if x < self.val:
                a = self.sag.supprimerABR(x)
                if a:
                    self.sag=None
                    a = False
            else:
                ##un seul fils à droite
                if x > self.val:
                    a = self.sad.supprimerABR(x)
                    if a:
                        self.sad = None
                        a = False
                ##deux fils
                else:
                    if self.sag is None:
                        if self.sad is None:
                            return True
                        else:
                            aux = self.sad
                            self.sad = None
                            self.val = aux.val
                            self.sad = aux.sad
                    else:
                        if self.sad is None:
                            if self.sag is None:
                                return True
                            else:
                                aux = self.sag
                                self.sag = None
                                self.val = aux.val
                                self.sag = aux.sag
                        ##suppression de la valeur max du sous arbre gauche
                        else:
                            y = self.sag.supprimerMAX()
                            if self.sag.val == y:
                                self.sag = None
                            self.val = y

    ##retourne vrai si l'élément x est dans l'arbre binaire de recherche courant
    def estpresent(self,x):
        res = False
        if self:           
            if x > self.val and self.sad:
                res = self.sad.estpresent(x)
            elif x < self.val and self.sag:
                res = self.sag.estpresent(x)
            else:
                return True
        return res

    ##affiche un abre verticalement afin de visualiser sa profondeur              
    def afficherModeArbre(self,x):         
        if self.sag:            
            self.sag.afficherModeArbre(x-1)
        print(2*x*" ",end="") 
        print("-",self.val)
        if self.sad:
            self.sad.afficherModeArbre(x-1)
        return ""
    
    ##affiche l'arbre binaire de recherche courant sous forme de chaine de caratère
    ##chaque élément est séparer par un ':' et le parcours de l'affichage est postfixe
    def afficherABR(self,res=""):
        if self:
            if self.sag:            
                res = self.sag.afficherABR(res)           
            if self.sad:
                res = self.sad.afficherABR(res)
            res = res + str(self.val) + ':'
        return res

    ##redefinition de la fonction print de python afin d'utiliser la fonction afficherABR()
    def __str__(self):
        return self.afficherABR()

