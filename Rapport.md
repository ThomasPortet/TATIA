# Description des taches

Pour ce projet, le but était de générer des titres d'articles sur internet dits "clickbait". Nous avons réalisé les taches suivantes :

* Nettoyer le data set pour être plus utilisable
* Extraire les fréquences des bigrammes des titres
* Stocker ses fréquences dans un format spécial pour ne pas avoir à recalculer
* Utiliser les fréquences pour générer des titres

# Détails de la conception et implémentation de l'algorithme/système

## Génération de titres

L'algorithme se base sur les fréquences de bigrammes pour générer les titres.

On mesure la fréquence de chaque bigramme de chaque titre du data set, en ajoutant des mots spéciaux pour signifier le début et la fin d'un titre.

On commence par le mot spécial de début, puis on prends un bigramme aléatoire commençant par ce mot dans tous les bigrammes trouvés, avec les bigrammes plus fréquent ayant une plus grande chance d'être choisis. On répète ce processus en utilisant le mot que l'on vient de rajouter au lieu du mot de départ.

Lorsque le mot spécial de fin de titre est choisi, on arrête la génération. Pour éviter les titres trop courts, on repart du début si un titre fini avec moins de 3 mots.

## Stockage des fréquences

Pour ne pas à recalculer les fréquences à chaque fois, elles sont calculées dans un autre programme qui stocke les résultats dans un fichier.

Le format de ce fichier est le suivant:

* Chaque "bloc" commence par un mot suivi du nombre de bigrammes qui commencent par ce mot, noté N
* Les N lignes qui suivent sont alors le mot finissant le bigramme et son nombre d'apparaitions dans le data set (soit sa fréquence)

Le mot spécial de début de titre est `_start_` et celui de fin est `_end_`.

# Jeux de données utilisés lors de l’expérimentation

https://www.kaggle.com/therohk/examine-the-examiner

Il s'agit d'une compilation de titres du site The Examiner, qui contient 3.09 millions de titres d'articles, ce site est réputé pour ses articles vite écrits avec des titres accrocheurs.

# Résultats obtenus (évaluation)

Les résultats sont parfois excellents, parfois un peu moins excellent, mais toujours divertissant.
Voici 10 phrases générées
```
Paris on Exercise equipment and returned to knit toys contain twists and is known museum visit patients
Apothederm SmartPeptide techology from all state of urgent medical emergency management
Cheetah Hunt for motocross
Bonded cats and Lofts at the Old Boys of September 1
UFC 126 A Supreme Court on U S Senate prefers Xbox 720 game s Day
Major league hit one
Recent dating Is RB Chris Gethard turns to Chris Brown party at TNA No Tofu with new Celebrity s on Celebrity Inspired People settle in the demise of abandoned at Lake Bruins
J Reed appeals to Rangers acquire Tumblr
Macy s economy bringing Star Cricket Live Action Well sung White House is oil shampoo
Apps Respond on American Revolution
```
# Analyse des erreurs

Il y en a, c'est avéré.

# Commentaires sur les améliorations possibles

On pourrait déduire la grammaire des titres et l'utiliser pour générer des titres plus convaincants. On pourrait compléter le data set avec des données plus récentes.
