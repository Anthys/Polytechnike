import time, copy

a = open("a_example.in", "r")
b = open("b_small.in", "r")
c = open("c_medium.in", "r")
d = open("d_quite_big.in", "r")
e = open("e_also_big.in")

dcp = copy.deepcopy

def donnees(fichier):
    txt = [line.split() for line in fichier]
    for i, x in enumerate(txt[1]):
        txt[1][i] = int(x)
    pizzas = txt[1]
    nbparts = int(txt[0][0])
    return pizzas, nbparts



def putain(mxx, pizzas, txt = True):
  S_sum = 0
  S_values = []
  S_index = []

  C_sum = 0
  C_values = []
  C_index = []

  pizzas.reverse() ## Reverse pour itérer de la pizza comportant la plus de part à celle qui en comporte le moins

  if txt: print("list", pizzas)

  prim_inx = 0
  done = False

  iters = 0

  while not done:
    iters += 1

    for i in range(prim_inx, len(pizzas)): # Boucle de base, ajout de pizzas tant que c'est possible
      if C_sum + pizzas[i] <= mxx:
        C_values += [pizzas[i]]
        C_sum += pizzas[i]
        C_index += [i]
      if C_sum == mxx:
        break
    
    if C_sum > S_sum: # Actualisation de la meilleure solution
      S_sum = C_sum
      S_values = dcp(C_values)
      S_index = dcp(C_index)
    
    if S_sum == mxx: # Sortir si la solution optimale a été trouvée.
      done = True
      break

    if txt: print("Alafaim",C_values, "sum", S_sum)

    done2 = False
    iter2 = 0

    while not done2: # Enlever la dernière pizza de la solution, recommencer à l'indice d'après en conservant le reste de la solution
      iter2 +=1
      tempv = C_values[-1]
      C_values = C_values[:-1]
      tempi = C_index[-1]
      C_index = C_index[:-1]
      C_sum -= tempv
      prim_inx = tempi+1
      
      if prim_inx < len(pizzas): # Si le nouvel indice est conforme, parfait. S'il sort de la liste, on refait un tour pour checker l'indice suivant
        done2 = True
      else:
        if len(C_values) == 0: #On a testé tout ce qu'on pouvait
          done=True
          break
      #if C_values == []:
      #  done = True
      #  break
      
      if txt:
        print("Apraitréteman",C_values, "sinx", prim_inx, "iter", iter2)
  
  return S_sum

#a = 100
#b = [1,10,10,12,40,40,55]

"""

l_n = ["a","b","c","d","e"]

if True:
  tpt = 0
  tpm = 0
  tA = time.time()
  for i,v in enumerate([a,b,c,d,e]):
    print("Testing",l_n[i],"...")
    pzz,nm = donnees(v)
    tm1 = time.time()
    res = putain(nm,pzz, False)
    tm2 = time.time()
    print("  Points = ", res, "/", nm)
    print("  Points manquants = ", nm-res)
    print("  Temps = ", tm2-tm1, "s")
    tpt += nm
    tpm += res
  print("----------")
  print("Total de point manquant:", tpt-tpm)
  print("Temps total:", time.time()-tA,"s")
"""


#pzz,nm = donnees(a)
#print(putain(nm,pzz))