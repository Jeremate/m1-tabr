#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import abr
import random
import time
import os


class OBJ:
    """
    Classe OBJ représentant chaque case de TABR.

    Attributs :
        - debut : Entier - valeur dé début de l'intervalle
        - fin : Entier - valeur de fin de l'intervalle
        - abr : ABR - ABR sans doublons dont tous les éléments se situent dans l'intervalle fermé
    """

    ## initialisation d'un objet
    def __init__(self,debut=None,fin=None):
        self.debut = int(debut) ##debut de la case
        self.fin = int(fin) ##fin de la case
        self.abr = abr.ABR() ##arbre binaire de recherche de la case

    ## affichage du contenu de l'objet
    def afficherOBJ(self):
        str_abr = self.abr.afficher()## appel de l'affichage d'un ABR
        return str(self.debut)+':'+str(self.fin)+';'+str_abr ##concaténation du resultat

    ## redefinition de la fonction print 
    def __str__(self):
        return self.afficherOBJ()

  
class TABR:
    """
    Définition de la classe TABR = tableau d'ABR.
    Chaque indice représente un type OBJ.
    """

    tab = []
    ## fonction permettant de lire le contenu d'un fichier externe contenant la description
    ## d'un TABR sous la forme 1:2;1:2 (debut:fin;arbre)
    def lireFichier(self,path):
        if os.path.exists(path):
            f = open(path,'r')
            for ligne in f:
                indiceDF,valABR = ligne.split(';')
                debut,fin = indiceDF.split(':')
                valAinserer = valABR.split(':')
                obj = OBJ(debut,fin)
                for i in reversed(valAinserer):
                    obj.abr.insererABR(int(i))
                TABR.tab.append(obj)
            f.close()
        else:
            print "fichier inconnu"

    ## fonction d'insertion d'un TABR dans un fichier text
    def ecrireFichier(self,adresse,nom):
        f = open(adresse+nom,'w')
        f.write(self.afficherTABR())
        f.close()

    ## création d'un TABR aléatoire
    ## n le nombre de case du TABR
    ## m le nombre fin de l'interval TABR[n]
    def tabrAleatoire(self,n,m):
        if TABR.tab != []:
            TABR.tab = []
        ## permet de crée les intervals debut|fin de chaque case
        b = random.sample(range(2,m-1),(n-1)*2)## retourne un ensemble d'element de taille (n-1)*1 comprit entre les éléments 2 et m-1
        b.append(1)
        b.append(m)
        b.sort()
        for i in range(0,len(b)-1):
            if i%2 == 0:
                debut = b[i]
                fin = b[i+1]
                ## permet de créer une liste d'élement à ajouter dans l'ABR d'une case
                val = random.sample(range(debut,fin),random.randint(1,fin-debut))
                obj = OBJ(debut,fin)
                for j in val:
                    obj.abr.inserer(int(j))
                TABR.tab.append(obj)                


    ## fonction qui verifie si le TABR courant est valide au spécification d'un TABR
    def verification(self):
        res = "Vide"
        a = 0
        if TABR.tab != []:
            for obj in TABR.tab:
                if obj.debut < a or obj.debut > obj.fin:
                    return "Non TABR"
                else:
                    a = obj.fin
                chaine = obj.abr.afficher().split(':')
                for valeur in chaine[:len(chaine)-1]:
                    if int(valeur) < obj.debut or int(valeur) > obj.fin:
                        return "Non TABR"
            res = "TABR valide"
        return res               

    ## fonction d'affichage d'un TABR
    ## appel l'affichage d'un objet qui appel l'affichage d'un ABR
    def afficherTABR(self):
        res =""
        for i in TABR.tab:
            res = res + i.afficherOBJ() +"\n"
        return res    

    ## insère x dans le TABR si un interval debut|fin le permet
    def insererEntier(self,x):
        for obj in TABR.tab:
            if obj.debut < x and obj.fin > x:
                obj.abr.inserer(x)

    ## supprime x dans le TABR si il existe
    def supprimerEntier(self,x):
        res = "x impossible dans les intervalles debut/fin"
        for obj in TABR.tab:
            if x > obj.debut and x < obj.fin:
                if obj.abr.estPresent(x) == True :
                    obj.abr.supprimer(x)
                    res="Valeur "+str(x)+" supprimé"
                else:
                    res = "x non présent dans l'ABR"
        return res

    ## fusion de deux cases du TABR courant les elements de la case i+1
    ## sont ajouté dans i
    def fusionTABR(self,i):
        if i < len(TABR.tab):
            str_abr = TABR.tab[i+1].abr.afficher()
            elem = str_abr.split(':')
            elem = elem[:len(elem)-1]
            TABR.tab[i].fin = TABR.tab[i+1].fin ## mise à jour de l'interval
            for valeur in elem: ## insertion des élément i+1 dans i
                TABR.tab[i].abr.inserer(int(valeur))
            TABR.tab.pop(i+1) ## suppression de l'objet en case i+1

    ## renvoie un ABR à partir du TABR courant
    def TABRversABR(self):
        A = abr.ABR()
        if TABR.tab != []:
            for obj in TABR.tab:
                str_abr = obj.abr.afficher()
                elem = str_abr.split(':')
                elem = elem[:len(elem)-1]
                for val in elem:
                    A.inserer(val)
        return A

    ## renvoie un TABR à partir de l'ABR courant
    def ABRversTABR(self):
        return 0
    
    ## redifition de la fonction print afin de pouvoir utiliser notre propre
    ## fonction d'affichage
    def __str__(self):
        return self.afficherTABR()

    ## supprimer le TABR courant
    def __del__(self):
        TABR.tab = []


##A = abr.ABR()
##T = TABR()
##T.lireFichier()
##print("lecture fichier :\n\n",T)
##print("vérification tabr : ",T.verification())
##T.fusionTABR(2)
##print("verification fusion :\n",T)
##print(T.supprimerEntier(2))
##print("vérification suppression :\n",T)
##T.tabrAleatoire(3,50)
##print("tabr aléatoire :\n\n",T)
##print("vérification tabr :\n\n",T.verification())
##print(T)
##A = T.TABRversABR()
##print(A)
##
##
##T.ecrireFichier("","exportABR.txt")
##del T
##T = TABR()
##print(T)
##T = TABR()
##T.tabrAleatoire(5, 11)
##print T
##del T

