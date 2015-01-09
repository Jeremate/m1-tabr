#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import abr
import random
import time
import os

# TODO JK :
# - faire les tests
# - ajouter au menu la fonction ABRversTABR

class OBJ:
    """
    Classe OBJ représentant chaque case de TABR.

    Attributs :
        - debut : Entier - valeur dé début de l'intervalle
        - fin : Entier - valeur de fin de l'intervalle
        - abr : ABR - ABR sans doublons dont tous les éléments se situent dans l'intervalle fermé
    """

    def __init__(self,debut=None,fin=None):
        """Initialisation d'un objet"""
        self.debut = int(debut) ##debut de la case
        self.fin = int(fin) ##fin de la case
        self.abr = abr.ABR() ##arbre binaire de recherche de la case

    
    def afficherOBJ(self):
        """Affichage du contenu de l'objet"""
        str_abr = self.abr.afficher()## appel de l'affichage d'un ABR
        return str(self.debut)+':'+str(self.fin)+';'+str_abr ##concaténation du resultat

     
    def __str__(self):
        """redefinition de la fonction print"""
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
                    obj.abr.inserer(int(i))
                TABR.tab.append(obj)
            f.close()
        else:
            print "fichier inconnu"

    ## fonction d'insertion d'un TABR dans un fichier text
    def ecrireFichier(self,path):
        f = open(path,'w')
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
    def inserer(self,x):
        res = False
        for obj in TABR.tab:
            if obj.debut <= x and obj.fin >= x:
                res = obj.abr.inserer(x)
        return res

    ## supprime x dans le TABR si il existe
    def supprimer(self,x):
        res = "x impossible dans les intervalles debut/fin"
        for obj in TABR.tab:
            if x >= obj.debut and x <= obj.fin:
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

    def ABRversTABR(self, A):
        """Renvoie un TABR à partir de l'ABR courant"""
        TABR.tab = []
        abr_str = A.afficher()
        list_val = abr_str.split(':')
        list_val.sort(key=int) # tri par ordre croissant

        k = 0
        while k < 1 or k > len(list_val):
            k = raw_input("Saisir le nombre d'intervalles : ")
            if k.isdigit():
                k = int(k)
            else:
                k = 0

        print "Renseigner les bornes max de chaque intervalle."
        for i in range(1, k):
            borne = 0
            borne_prec = borne
            # vérfication de la saisie de la borne
            while borne < 1 or borne < borne_prec:
                borne = raw_input("\t- Intervalle " + str(i) + " : ")
                if borne.isdigit():
                    borne = int(borne)
                    # la borne supérieure doit être inférieure au max de l'ABR et supérieure au min
                    # la borne supérieure de l'intervalle courant doit laisser au moins une valeur pour les prochains intervalles
                    if borne < int(list_val[0]) or borne > int(list_val[len(list_val)-1]) or k-i > len([val for val in list_val if int(val) > borne]):
                        print "Borne invalide"
                        borne = 0
                else:
                    print "Borne invalide"
                    borne = 0
            # cas particulier de la première borne (=min de l'ABR)
            if (i == 1):
                deb = int(list_val[0])
            else:
                deb = int(next(val for val in list_val if int(val) > borne_prec))
            # print deb, borne
            obj = OBJ(deb, borne)
            for val in [val for val in list_val if int(val) >= deb and int(val) <= borne]:
                obj.abr.inserer(int(val))
            TABR.tab.append(obj)

            borne_prec = borne # mémorisation de la borne précédente
         
        # cas particuluer de la dernière borne (=max de l'ABR)
        deb = int(next(val for val in list_val if int(val) > borne_prec))
        fin = int(list_val[len(list_val)-1])
        print "Intervalle " + str(k)
        print deb, fin
        obj = OBJ(deb, fin)
        for val in [val for val in list_val if int(val) >= deb]:
            obj.abr.inserer(int(val))
        TABR.tab.append(obj)

    
    ## redifition de la fonction print afin de pouvoir utiliser notre propre
    ## fonction d'affichage
    def __str__(self):
        return self.afficherTABR()

    ## supprimer le TABR courant
    def __del__(self):
        TABR.tab = []


A = abr.ABR()
T = TABR()
# T.lireFichier("fichier.txt")
# print("lecture fichier :\n\n",T)
# print("vérification tabr : ",T.verification())
A.inserer(9)
A.inserer(6)
A.inserer(3)
A.inserer(7)
A.inserer(12)
print A
T.ABRversTABR(A)
print("vérification tabr : ",T.verification())
print T
del A
del T
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

