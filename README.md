# Polytechnike

[HashCode 2020](#HashCode-2020)

​	[HashCode 2020 contest](hashcode-2020--google-books)

[HashCode 2021](#Hashcode-2021)

​	[HashCode 2021 contest](#hashcode-2021---traffic-lights)

# HashCode 2020

## Practice

### Problème des pizzas

#### Pistes

[Lien vers les pistes.](2020/Pizza/PistePizza.md)

#### Le 29/01

Il nous manque 253 points sur 1 505 004 617.

#### Le 02/02

Il nous manque 1 point théorique sur 1 505 004 617, mais 0 en réalité. La solution proposée trouve le résultat optimal, mais le fait qu'elle termine rapidement repose probablement sur la chance/composition des listes (il est necessaire qu'il y ait une solution parfaite dans la liste, et qu'elle soit accessible rapidement, sinon le programme pourrait y passer plusieurs années).

### Problème du slideshow

#### Solution droite-gauche

On ajoute linéairement chacune des slides soit à droite soit à gauche du diapo précédent. On obtient **373241** points, et 24 points pour le jeu de donnée B.

#### Solution gloutonne complète

On cherche la meilleure diapo à foutre à droite dans les N suivantes. Pour N=10, on obtient **518747** points, et la solution prend mille ans à être calculée.

## HASHCODE 2020 | Google Books

[Résulats précis, analyses complètes, etc...](2020/coconut/Heysalutatouslesamiscestdavidlafargepokemonjesperequevousallezbienaujourdhui.md)

### Résultat global
- 103 français
- 1424 mondial

### Pistes pour faire mieux, ou la préquelle du top 1 de 2021
- Prendre un peu de temps pour pondérer les formules décidées: Afin de simplifier la solution, on a décidé d'appliquer une certaine valeur d'efficacité à chaque librairie, calculée avec une certaine fonction mathématique prenant plusieurs paramètres (temps de signup, nombre de points...). On aurait pu pondérer chacun des termes ou les changer un peu pour gagner quelques points.
- Prendre du temps pour analyser chacun des sets, ça nous permettrait de trouver les failles de nos programmes, les cas limites, etc.
- Faire directement une fonction de calcul des points, ce qui nous permettrait de faire des itérations pour trouver les meilleures.

# HashCode 2021 

## Practice round

731 000 000 points, on a pas trouvé mieux sur internet, donc top 1 monde par défaut.
On a gagné les derniers points en faisant jouer des coefficients sur notre fonction principale qui choisit la pizza la plus adaptée.

## HASHCODE 2021 - Traffic lights

[Link](2021/traffic-lights/traffic-lights.md)