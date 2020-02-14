# Polytechnike


# Problème des pizzas

### Pistes

[Lien vers les pistes.](PistePizza.md)

### Le 29/01

Il nous manque 253 points sur 1 505 004 617.

### Le 02/02

Il nous manque 1 point théorique sur 1 505 004 617, mais 0 en réalité. La solution proposée trouve le résultat optimal, mais le fait qu'elle termine rapidement repose probablement sur la chance/composition des listes (il est necessaire qu'il y ait une solution parfaite dans la liste, et qu'elle soit accessible rapidement, sinon le programme pourrait y passer plusieurs années).

# Problème du slideshow

### Solution droite-gauche

On ajoute linéairement chacune des slides soit à droite soit à gauche du diapo précédent. On obtient **373241** points, et 24 points pour le jeu de donnée B.

### Solution gloutonne complète

On cherche la meilleure diapo à foutre à droite dans les N suivantes. Pour N=10, on obtient **518747** points, et la solution prend mille ans à être calculée.
