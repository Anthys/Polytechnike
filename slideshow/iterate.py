from charger_fichier import *
from slide1 import *
from georgelin_marc import *
from retourner_fichier import *
from regroupe_V import *


def iterate_pics(liste):
  lentot = len(liste)
  out = [liste[0]]
  liste = liste[1:]
  while not liste == []:
    tvalmax = -1
    timax = -1
    for i,v in enumerate(liste):
      if i > 10:
        break
      #print(points_of_transi(out[-1], v))
      if points_of_transi(out[-1], v) > tvalmax:
        tvalmax = points_of_transi(out[-1], v)
        timax = i
    out += [liste[timax]]
    liste = liste[:timax] + liste[timax+1:]
    print(str(len(out)/lentot*100) + "%")
  return out

def points_of_transi(image1, image2):
  a_arg = image1["arg"]
  b_arg = image2["arg"]
  inter1 = inter(a_arg, b_arg)
  diff1 = difference(a_arg, b_arg)
  diff2 = difference(b_arg, a_arg)
  return min(len(inter1), len(diff1), len(diff2))

import os 

name_file = "michel.tx"

michel = open(name_file, "a+")
michel.write("\n\n")
michel.write("SOLUTION ITERATE\n")
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
        T = tri_images(T)
        res = iterate_pics(T)
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