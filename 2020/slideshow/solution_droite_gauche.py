from charger_fichier import *
from slide1 import *
from georgelin_marc import *
from retourner_fichier import *
from regroupe_V import *

name_file = "mireille.tx"

michel = open(name_file, "a+")
michel.write("\n\n")
michel.write("SOLUTION DROITE GAUCHE\n")
michel.write("\n\n")
michel.close()
total = 0
for i in os.listdir():
    if i[-4:] == ".txt":
        print("Processing ... ", i)
        a = load(i)
        V,H = liste_verticale(a)
        V = trier_verticale(V)
        M = regroupe_V(V)
        T = M + H
        res,t = final(T) 
        res = compter_nombre_points(res)
        print(" nb points : ", res)
        michel = open(name_file, "a+")
        michel.write("for "+i+" :\n")
        michel.write(" nb points : "+ str(res)+"\n")
        michel.close()
        total += res

michel = open(name_file, "a+")
michel.write("TOTAL : "+ str(res)+"\n")
michel.close()
print("Total", res)