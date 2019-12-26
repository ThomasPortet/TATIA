# Projet TATIA

Groupe : 
* Thomas Portet
* Aymeric Picard Marchetto

# Utilisation

```python main.py data/data.txt [nb]```

Génère `[nb]` titres aléatoires en utilisant notre jeu de données. Fonctionne sur linux avec python 3.

# Autre fichiers

## Programmes

* `cleanSource.py` a servi pour nettoyer le data set original (`examiner-date-text.csv`) en format plus lisible (`cleanedSource.txt`)
* `genProba.py` transforme un fichier de titres bruts (`cleanedSource.txt`) avec les données des bigrammes pour le programme (`data.txt`)

## Données

* `dataraw` contient les données non traitées
  * `examiner-date-text.csv` est le data set original tel quel (zippé pour prendre moins de place)
  * `cleanedSource.txt` le data set nettoyé par `cleanSource.py` (zippé pour prendre moins de place)
  * `smallDataTest.txt` un data set artificiel pour tester l'algorithme
* `data` contient les données prêtes à l'emploi
  * `data.txt` les données générées par `genProba.py` à partir de `cleanedSource.txt`
  * `dataSmall.txt` les données générées par `genProba.py` à partir de `smallDataTest.txt`

Source du data set : https://www.kaggle.com/therohk/examine-the-examiner
