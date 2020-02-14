__author__ = 'julesmichaud'
__filename__ = 'regroupe_V.py'
__date__ = '14/02/20'

from charger_fichier import *
from slide1 import *
from georgelin_marc import *
from retourner_fichier import *


def regroupe_V(liste):
    '''Regroupe les éléments V sous forme de TUPLES auxquels on a modifié les arguments'''
    new_liste = []
    while len(liste) != 0:
        if len(liste) != 1:
            indice_1 = 0#liste[0]
            maximum = 0
            indice_2 = 0
            for i in range(1, min(6, len(liste))):
                a = min(len(difference(liste[indice_1]['arg'], liste[indice_1 + i]['arg'])),
                        len(difference(liste[indice_1 + i]['arg'], liste[indice_1]['arg'])),
                        len(inter(liste[indice_1]['arg'], liste[indice_1 + i]['arg'])))
                if a >= maximum:
                    maximum = a
                    indice_2 = i
            new_liste += [{'indice': (liste[indice_1]['indice'], liste[indice_2]['indice']),
                           'arg': union(liste[indice_1]['arg'], liste[indice_2]['arg'])}]
            new_liste[-1]["nb_arg"] = len(new_liste[-1]["arg"])
            del liste[indice_2]
            del liste[indice_1]
        else:
            new_liste += [{'indice': liste[0]['indice'], 'arg': liste[0]['arg'], 'nb_arg': liste[0]['nb_arg']}]
            del liste[0]
    return new_liste

import os 
for i in os.listdir():
    total = 0
    if i[-4:] == ".txt":
        print("Processing ... ", i)
        a = load(i)
        V,H = liste_verticale(a)
        V = trier_verticale(V)
        M = regroupe_V(V)
        #print(V)
        #print(M)
        T = M + H
        res,t = final(T) 
        res = compter_nombre_points(res)
        print(" nb points : ", res)
        total += res
print("Total :", total)