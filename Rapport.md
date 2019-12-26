# Description des taches

Pour ce projet, le but était de générer des titres d'articles sur internet dits "clickbait". Nous avons réalisé les taches suivantes :

* Nettoyer le data set pour être plus utilisable
* Extraire les fréquences des bigrammes des titres
* Stocker ses fréquences dans un format spécial pour ne pas avoir à recalculer
* Utiliser les fréquences pour générer des titres

# Détails de la conception et implémentation de l'algorithme/système

Nous avons utilisé l'algorithme des bigrammes pour générer les couples de mots les plus probables de se suivre.

On a introduit un début de phrase et un fin de phrase pour que les phrases générées commencent et terminent avec des mots qui ont de forte probabilité d'être en début ou fin de phrase.

# Jeux de données utilisés lors de l’expérimentation

https://www.kaggle.com/therohk/examine-the-examiner

Il s'agit d'une compilation de titres du site The Examiner, qui contient 3.09 millions de titres d'articles, ce site est réputé pour ses articles vite écrits avec des titres accrocheurs.

# Résultats obtenus (évaluation)

Les résultats sont parfois excellents, parfois un peu moins excellent, mais toujours divertissant.

# Analyse des erreurs

Il y en a, c'est avéré.

# Commentaires sur les améliorations possibles

On pourrait déduire la grammaire des titres et l'utiliser pour générer des titres plus convaincants. On pourrait compléter le data set avec des données plus récentes.
