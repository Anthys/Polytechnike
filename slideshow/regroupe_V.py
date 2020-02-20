__author__ = 'julesmichaud'
__filename__ = 'regroupe_V.py'
__date__ = '14/02/20'

from charger_fichier import *
from slide1 import *


def regroupe_V(liste):
    '''Regroupe les éléments V sous forme de TUPLES auxquels on a modifié les arguments'''
    new_liste = []
    while len(liste) != 0:
        if len(liste) == 1:
            indice_1 = liste[0]
            maximum = 0
            indice_2 = 0
            for i in range(1, min(6, len(liste))):
                a = min(difference(liste[indice_1]['arg'], liste[indice_1 + i]['arg']),
                        difference(liste[indice_1 + i]['arg'], liste[indice_1]['arg']),
                        inter(liste[indice_1]['arg'], liste[indice_1 + i]['arg']))
                if a >= maximum:
                    maximum = a
                    indice_2 = i
            new_liste += [{'indice': (liste[indice_1]['indice'], liste[indice_2]['indice']),
                           'nb_arg': liste[indice_1]['nb_arg'] + liste[indice_2]['nb_arg'],
                           'arg': union(liste[indice_1]['arg'], liste[indice_2]['arg'])}]
            del liste[indice_1]
            del liste[indice_2]
        else:
            new_liste += [{'indice': liste[0]['indice'], 'arg': liste[0]['arg'], 'nb_arg': liste[0]['nb_arg']}]
            del liste[0]
    return new_liste


a = load("e_shiny_selfies.txt")
V = trier_verticale(liste_verticale(a))
M = regroupe_V(V)
print(V)
print(M)
