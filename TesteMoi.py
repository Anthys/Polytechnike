import time

import putain


a = open("a_example.in", "r")
b = open("b_small.in", "r")
c = open("c_medium.in", "r")
d = open("d_quite_big.in", "r")
e = open("e_also_big.in")

l_n = ["a","b","c","d","e"]

def donnees(fichier):
    txt = [line.split() for line in fichier]
    for i, x in enumerate(txt[1]):
        txt[1][i] = int(x)
    pizzas = txt[1]
    nbparts = int(txt[0][0])
    return pizzas, nbparts

tpt = 0
tpm = 0
tA = time.time()
for i,v in enumerate([a,b,c,d,e]):
  print("Testing",l_n[i],"...")
  pzz,nm = donnees(v)
  if i == 4:
    print(len(pzz))
    pzz = pzz[:500]
  tm1 = time.time()
  res = putain.putain(nm,pzz, False)
  tm2 = time.time()
  print("  Points = ", res, "/", nm)
  print("  Points manquants = ", nm-res)
  print("  Temps = ", tm2-tm1, "s")
  tpt += nm
  tpm += res
print("----------")
print("Total de point manquant:", tpt-tpm)
print("Temps total:", time.time()-tA,"s")