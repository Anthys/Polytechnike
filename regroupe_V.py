__author__ = 'julesmichaud'
__filename__ = 'regroupe_V.py'
__date__ = '14/02/20'

from charger_fichier import *
from slide1 import *


def regroupe_V(liste):
    '''Regroupe les éléments V sous forme de TUPLES auxquels on a modifié les arguments'''
    new_liste = []
    for indice in range(len(liste)):
        if indice < len(liste) - 5:
            max = 0
            for i in range(1, 6):
                a = min(difference(liste[indice], liste[indice + i]), difference(liste[indice + i], liste[indice]),
                        inter(liste[indice], liste[indice + i]))
                if a > max:
                    max = a
        else:
            i_max = len(liste) - indice
            max = 0
            for i in range(1, i_max):
                a = min(difference(liste[indice], liste[indice + i]), difference(liste[indice + i], liste[indice]),
                        inter(liste[indice], liste[indice + i]))
                if a > max:
                    max = a


a = load("qualification_round_2019.in/e_shiny_selfies.txt")
