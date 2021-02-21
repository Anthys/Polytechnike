1. Une solution pour des petits ensembles
      - Factorielle, récursive
      - Trop couteuse
2. Une solution pour les plus grandes ensembles
   - Étiquetage des pizzas en ensemble "petits", "moyens", "grands", {Linéaire}
   - Choix d'un certain nombre de pizza grandes, puis de moyennes, puis de petites. On se retrouve avec une solution relativement rapidement.
   - Le choix peut être borné par un certain pourcentage (exemple on prend des pizzas grandes jusqu'à atteindre 50% de la solution).
   - Optionel: (améliorer encore la solution trouvée rapidement)
       - Echanges de pizzas petites entre petites pour limiter encore le débordement
       - Arrêt lorsqu'on arrive au delà d'un certain pourcentage de la solution (99%), et on rend la solution. On peut calculer la somme toutes les n opérations.
   - On peut mettre plusieurs ensembles, par exemple "très grand", "grand", "moyen", "petit", "très petit", le nombre d'ensemble peut dépendre du nombre de pizzas.
3. Idem, ensembles grands.
   - Calculer la moyenne, prendre autour de la moyenne -> Revient un peu à la solution d'avant, mais on ne prend que des moyens
4. Solution organique, aléatoire
   - Nulle car aléatoire, mais les solutions peuvent être bien meilleures que celles de bases, même avec peu d'itérations
6. Solution pour tout:
   - Trier la liste, prendre toutes les premières pizzas jusqu'à déborder, puis enlever la pizza la plus intéréssante de la combinaison conservée (ceelle la plus proche de la valeur de débordement)
   - Très rapide, mais si les termes intéressants sont en bout de file, un peu chiant
   - Compliqué d'améliorer la solution vu qu'il faudrait échanger des termes de fin de file (donc gros car la liste est triée) et échanger avec beaucoup de petits
7. Une solution pour tout:
   - En {n²}, on part de la fin de la liste triée et on remplit comme on peut, puis on réitère en enlevant le dernier terme.
8. Une solution pour tout, améliorée:
   - On remplit comme on peut, comme la solution précédente, puis on recommence en enlevant juste le dernier terme de la dernière solution trouvée, en conservant le reste de la solution intact. Ca ressemble à du factoriel, mais sur les listes de Google, le total du temps est en dessous de la seconde.
   - On pourrait améliorer cette solution sans se baser sur la chance, en switchant de programme au bout de n itérations. On compare alors la meilleure solution de cet algorithme avec celle de (7).
   - On peut également calculer la solution en n², puis lancer l'algorithme 8 et s'arreter dès qu'on a une meilleure solution.