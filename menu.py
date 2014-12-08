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

while True:
    print("1 - Génération, sauvegarde et affichage de TABR")
    print("2 - Manipulation de TABR")
    print("3 - Exit")
    selection = input("Sélectionner action:")
    if selection == '1':
        for i in range(0,len(menu)):
            print(i+1,'-',menu[i])
        selection = input("Sélectionner action:")
        if selection == '1':
            T = TABR()
            print("Affichage du TABR chargé depuis un fichier :")
            print(T)
        elif selection == '2':
            adresse = input("Adresse où enregistrer le fichier")
            nom = input("Nom du fichier")
            T.ecrireFichier(adresse,nom)
        elif selection == '3':
            print(T)
        elif selection == '4':
            T.tabrAleatoire()
        elif selection == '5':
            print(T.verification())
        elif selection == '6':
            break
        else:
            print("Sélection non autorisé!")
    elif selection == '2':
        for i in range(0,len(menu2)):
            print(i+1,'-',menu2[i])
            selection = input("Sélectionner action:")
            if selection == '1':
                x 
            elif selection == '2':
                print(menu2[selection])
            elif selection == '3':
                print(menu2[selection])
            elif selection == '4':
                print(menu[selection])
            elif selection == '5':
                print(menu[selection])
            elif selection == '6':
                break
            else:
                print("Sélection non autorisé!")
    elif selection == '3':
        break
    else:
        print("Sélection non autorisé!")
             
