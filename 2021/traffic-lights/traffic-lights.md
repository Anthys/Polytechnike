# Traffic lights - HashCode 2021

**8,936,533** points - **2622** monde - **231** France

## Structures de données:

- Une liste `streets` dont chaque élément est un dictionnaire d'une route: `{"nom":"nom1", "taille":2, "istart":2, "iend":4} ` avec `iend` et `istart` qui sont les indices des intersections qui définissent les extrémités de la liste.
- Un dictionnaire dont les clés sont les noms des rues et les valeurs sont les indices correspondant aux nom, dans la liste `streets`.
- Une matrice de taille n_Intersections^2 . Mat\[i][j] donne l'indice de la route reliant l'intersection i à j si elle existe, -1 sinon.

- Une liste d'output de taille n_intersections. Chaque élément est une liste de feux qui seront placés à cette intersection. Chaque feu est un dictionnaire contenant l'indice de la route où est placé le feu, et la durée de fonctionnement.

## Algorithme

Naif:

Prendre toutes les routes, mettre un feu qui dure 1 seconde. Ça nous donne déjà énormément de points, le reste ne nous en a pas fait gagner énormément plus.

1:

Calculer les "densités" de chaque route, c'est à dire le nombre de voitures qui passeront sur chacune des routes. 

> Problème: on ne prend pas en compte l'évolution du graphe, on considère qu'il est à temps fixe

Pour les routes qui ont une densité nulle, laisser un feu rouge constamment. Pour les routes qui ont une forte densité, laisser le feu vert allumé plus longtemps.

Notre implémentation de la deuxième partie n'a pas semblé fonctionner, car les points qu'on obtenait étaient identiques à ceux obtenus sans cette méthode.

2:

Laisser un feu vert allumé longtemps quand: il est parcouru par beaucoup de voitures et qu'il est parcouru par des voitures à court trajet. En effet, on gagne des points par voitures, et on gagne plus de points si on les fait finir vite.

## Étude

Google donnait à disposition une visualisation du graphe des routes, ultra pratique. On aurait du perdre moins de temps a faire nos études par code nous même. Si la visualisation n'était pas disponible, cela aurait par contre vraiment valu le coup de le faire.

## CCL

+

Je pense que faire une fonction allant chercher les données dans la matrice était une bonne idée, cela a empêché de créer plus de confusion au moment de débugger nos programmes.

On a trouvé une manière de faire une fonction variable dépendant de coefficients (nb de voitures passant * a + nb de voitures passant si le trajet est court *b + taille de la route * c). On a pas réussi à la faire marcher, mais ça nous aurait permit de gagner plus de points.

https://codeshare.io/ était je pense plus pratique que Github, on pouvait se partager le code en quasi temps réel. Au début, on a pu partager les nomenclatures des structures de données qu'on voulait utiliser afin d'éliminer toute ambiguïté possible.

Je pense que c'est bien de ne pas démarrer immédiatement au début, mais de prendre le temps de discuter des structures de données, de la première piste qu'on veut explorer. S'assurer que cette piste est améliorable (si on fait un algo naif mais qu'on ne peut pas l'améliorer, il ne sert à rien). Prévoir un peu en avance ce qu'on peut faire.

On a coder la liste "densitées" des routes servant à améliorer la solution naive, en même temps que la solution naive. Je pense que c'était vraiment pertinent, pcq ça a permis d'améliorer le naif presque immédiatement, là ou le faire après aurait pu créer un temps mort.

-

Je pense qu'on ne s'est pas tous mis d'accord, ou on était pas tous au même niveau, par rapport aux traitements des structures de données.
Certains ont créés plusieurs structures intermédiaires (exemple au niveau des densités), il aurait peut-être mieux fallu ne pas les créer du tout, juste les prendre en argument de la fonction, ça a créer quelques ambiguïtés au moment de partager les programmes.

un tableau veleda ou rien

Si on avait été 1 de plus, je pense que cela aurait vraiment valu le coup de coder la simulation du problème (qui calcule également les points, mais surtout déplace les voitures). Elle ne me semble pas ultra compliqué, juste un peu longue à coder. Quelqu'un de suffisamment expérimenté aurait pu la coder avant la fin du temps, et avec cette simulation, on aurait pu savoir presque directement quels feux rouges passer à vert en fonction de la demande en temps réel. Ou alors se séparer en sous-équipes de 2: deux font la solution "temps fixe" que nous avons fait, deux autres font la solution "temps réel".

Il faut être sûr que ses fonctions marchent bien avant de les envoyer aux autres, les débugger pour des petites fautes de frappes peut rendre fou. Je pense qu'il faut se mettre d'accord sur des petits tests à faire avant.

Je me DEMANDE si manger pendant l'épreuve c'était pas une meilleure idée. Ça faisait une petite pause, permettait de réfléchir à tout ce qu'on faisait. On a que deux concours pour comparer donc j'en sais rien.