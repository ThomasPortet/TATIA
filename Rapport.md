# Description des taches

Pour ce projet, le but était de générer des titres d'articles sur internet dits "clickbait". Nous avons réalisé les taches suivantes :

* Nettoyer le data set pour être plus utilisable
* Extraire les fréquences des bigrammes des titres
* Stocker ses fréquences dans un format spécial pour ne pas avoir à les recalculer
* Utiliser les fréquences pour générer des titres

# Détails de la conception et implémentation de l'algorithme/système

## Génération de titres

L'algorithme se base sur les fréquences de bigrammes pour générer les titres.

On mesure la fréquence de chaque bigramme de chaque titre du data set, en ajoutant des mots spéciaux pour signifier le début et la fin d'un titre.

On commence par le mot spécial de début, puis on prends un bigramme aléatoire commençant par ce mot dans tous les bigrammes trouvés, avec les bigrammes plus fréquent ayant une plus grande chance d'être choisis. On répète ce processus en utilisant le mot que l'on vient de rajouter au lieu du mot de départ.

Lorsque le mot spécial de fin de titre est choisi, on arrête la génération. Pour éviter les titres trop courts, on repart du début si un titre fini avec moins de 3 mots.

## Stockage des fréquences

Pour ne pas avoir à recalculer les fréquences à chaque fois, elles sont calculées dans un autre programme qui stocke les résultats dans un fichier.

Le format de ce fichier est le suivant:

* Chaque "bloc" commence par un mot suivi du nombre de bigrammes qui commencent par ce mot, noté N
* Les N lignes qui suivent sont alors le mot finissant le bigramme et son nombre d'apparaitions dans le data set (soit sa fréquence)

Le mot spécial de début de titre est `_start_` et celui de fin est `_end_`.

# Jeux de données utilisés lors de l’expérimentation

https://www.kaggle.com/therohk/examine-the-examiner

Il s'agit d'une compilation de titres du site The Examiner, qui contient 3.09 millions de titres d'articles, ce site est réputé pour ses articles vite écrits avec des titres accrocheurs.

# Résultats obtenus (évaluation)

Les résultats sont de qualité variable mais sont souvent drôles. Voici 10 phrases générées :

```
The Pacific Standard will make first excerpt of Georgia Tech basketball substate opener to benefit from Aerospace Scholar Program
150 animals removed from show Belmont
Suggested changes to JUDO International Year
Adam Lambert responds to Christmas sales and Xbox 720 screen at 92
Pagans come from Elf Day Video
10 Olympic Training Week March 3 2012 RITA award
Randy Couture in the water is coming July 2 promo teases her body at Wake n Sun run
Sons of it s Rosie O P crowned
Cheryl Cole Konrad to appear along The Rock N Paws and star Charice talks The Hardest person stories
Basketball Wives fights
```

Les titres sont de longueur très variable et de cohérence très variable. Mais tout de même certains pourraient être des titres de vrais articles, comme on peut le constater avec certaines des phrases ci-dessus.

# Commentaires sur les améliorations possibles

On pourrait déduire la grammaire des titres et l'utiliser pour générer des titres plus convaincants. On pourrait compléter le data set avec des données plus récentes.
