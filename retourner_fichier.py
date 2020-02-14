from slide1 import *

def retourner_fichier(liste):
  txt = ""
  txt += str(len(liste))
  for i in liste:
    txt += i["indice"]
  return txt

def compter_nombre_points(liste):
  total = 0
  for i,v in enumerate(liste):
    if i< len(liste)-1:
      a_arg = v["arg"]
      b_arg = v["arg"]
      union1 = union(a_arg,b_arg)
      diff1 = difference(a_arg, b_arg)
      diff2 = difference(b_arg, a_arg)
      total += min(len(union1), len(diff1), len(diff2))
  return total
