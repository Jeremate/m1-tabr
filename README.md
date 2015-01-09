m1-tabr
=======

Projet en python sur les tableaux d'ABR

Sujet
-----
Nous considérons dans ce projet une structure de données appelée tableau d’ABR (abrégée TABR). Il s’agit d’un tableau T dont chaque case i correspond à un intervalle fermé T[i].debut...T[i].fin. Les informations stockées dans la case i sont T [i].debut, T [i].f in et un pointeur T [i].arbre vers un ABR sans doublons dont tous les éléments se situent dans l’intervalle fermé T [i].debut . . . T [i].f in. Les intervalles ont les propriétés suivantes :
(a) Ils sont bien définis : pour tout i,T[i].debut≤T[i].fin;
(b) Ils sont tous disjoints : deux intervalles différents n’ont aucun élément en commun ;
(c) Ils sont ordonnés par ordre croissant : pour tout i (sauf le dernier), T [i].f in < T [i + 1].debut.
Les extrémités T [i].debut, T [i].f in de chaque intervalle sont des entiers, et les éléments dans les ABR indiqués
par les pointeurs T [i].arbre sont également des entiers.

Exécution
---------
1) Se rendre dans le répertoire des sources : cd sources/
2) exécuter la commande suivante : python menu.py