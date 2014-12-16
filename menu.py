#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import tabr

menu = []
menu.append("Fichier vers TABR")
menu.append("TABR vers fichier")
menu.append("Affichage sur l'écran")
menu.append("TABR aléatoire")
menu.append("Vérification")
menu.append("Exit")
menu2 = []
menu2.append("Insertion d'un entier")
menu2.append("Suppression d'un entier")
menu2.append("Fusion de deux cases du TABR")
menu2.append("ABR vers TABR")
menu2.append("TABR vers ABR")
menu2.append("Exit")
courant = tabr.TABR()
while True:
    print("1 - Génération, sauvegarde et affichage de TABR")
    print("2 - Manipulation de TABR")
    print("3 - Exit")
    selection = raw_input("Sélectionner action:")
    if selection == '1':
        while True:
            for i in range(0,len(menu)):
                print i+1,'-',menu[i]
            selection = raw_input("Sélectionner action:")
            if selection == '1':
                path = raw_input("Path du fichier :")
                if os.path.exists(path):
                    print("Affichage du TABR chargé depuis un fichier :")
                    courant.lireFichier(path)
                    print "_____________________"
                    print courant
                else:
                    print "Erreur path"
            elif selection == '2':
                path = raw_input("Indiquer le chemin du fichier fichier :")
                if "/" in path:
                    if os.path.exists(path):
                        courant.ecrireFichier(path)
                        print "Fichier enregistrer"
                    else:
                        print "Path invalide!"
                else:
                    courant.ecrireFichier(path)
                    print "Fichier enregistrer"
            elif selection == '3':
                if courant.tab != []:
                    print courant
                else:
                    print "TABR vide"
            elif selection == '4':
                while True:
                    n = raw_input("Nombre de case pour le TABR :")
                    if int(n) >0:
                        break
                while True:
                    m = raw_input("Valeur pour T[n].fin :")
                    if int(m) > int(n)*2:
                        break
                courant.tabrAleatoire(int(n),int(m))
                print "_____________________"
                print courant
            elif selection == '5':
                print "Vérification si le TABR est bien formé"
                print courant.verification()
            elif selection == '6':
                break
            else:
                print("Sélection non autorisé!")
    elif selection == '2':
        while True:
            for i in range(0,len(menu2)):
                print i+1,'-',menu2[i]
            selection = raw_input("Sélectionner action:")
            if selection == '1':
                x = raw_input("Indiquer l'entier à insérer:")
                if courant == []:
                    print "TABR courant vide, impossible d'insérer"
                else:
                    if courant.inserer(int(x)):
                        print x," inséré"
                    else:
                        print x," n'a pas pu être inséré"
            elif selection == '2':
                x = raw_input("Indiquer l'entier à supprimer:")
                if courant == []:
                    print "TABR courant vide, impossible d'supprimé"
                else:
                    if courant.supprimer(int(x)):
                        print x," supprimé"
                    else:
                        print x," n'a pas pu être supprimé"
            elif selection == '3':
                print(menu2[int(selection)])
            elif selection == '4':
                print(menu2[int(selection)])
            elif selection == '5':
                print(menu2[int(selection)])
            elif selection == '6':
                break
            else:
                print("Sélection non autorisé!")
    elif selection == '3':
        break
    else:
        print("Sélection non autorisé!")
             
