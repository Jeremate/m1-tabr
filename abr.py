#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# TODO JK :
# - test si ABR non filiforme

class ABR:
    """
    Classe ABR représentant un arbre binaire de recherche.
    Pour rappel, les propriétés d'un ABR sont les suivantes :
        - les éléments contenus dans les noeuds du sag sont tous inférieurs ou égaux à val
        - les éléments contenus dans les noeuds du sad sont tous supérieurs à val

    Attributs :
        - val : entier - valeur du noeud
        - sag : ABR - le sous arbre gauche
        - sad : ABR - le sous arbre droit
    """

    ##fonction d'initialisation
    def __init__(self):
        self.val = None ##valeur du noeud - initialiser à vide
        self.sag = None ##sous arbre gauche - initialiser à vide
        self.sad = None ##sous arbre droit - initialiser à vide

    ## fonction qui insère un élément x dans l'arbre binaire de recherche courant
    ## l'ABR ne possède pas de doublons grâce à l'utilisation des inégalités strictes
    def inserer(self, x):
        res = True
        if self.val is None:
            self.val = x
        else:
            if x < self.val:
                if self.sag is None:
                    self.sag = ABR()
                self.sag.inserer(x)
            elif x > self.val:
                if self.sad is None:
                    self.sad = ABR()
                self.sad.inserer(x)
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

    ##fonction de suppression d'un élément x de l'abre binaire de recherche courant
    def supprimer(self,x):
        a = False
        if self is not None:
            ## un seul fils à gauche
            if x < self.val:
                a = self.sag.supprimer(x)
                if a:
                    self.sag=None
                    a = False
            else:
                ##un seul fils à droite
                if x > self.val:
                    a = self.sad.supprimer(x)
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
    def estPresent(self,x):
        res = False
        if self:          
            if x > self.val and self.sad:
                res = self.sad.estPresent(x)
            elif x < self.val and self.sag:
                res = self.sag.estPresent(x)
            elif self.val == x:
                res = True
        return res
    
    ##affiche l'arbre binaire de recherche courant sous forme de chaine de caratère
    ##chaque élément est séparer par un ':' et le parcours de l'affichage est suffixe
    def afficher(self,res=""):
        if self:
            if self.sag:            
                res = self.sag.afficher(res)           
            if self.sad:
                res = self.sad.afficher(res)
            if res:
                res += ':' + str(self.val)
            else:
                res = str(self.val)
        return res

    ##redefinition de la fonction print de python en utilisant la fonction afficher()
    def __str__(self):
        return self.afficher()
