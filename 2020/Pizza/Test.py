__author__ = "maxime"
__file__ = "Test.py"
__date__ = "28/01/20"

import time

a = open("a_example.in", "r")
b = open("b_small.in", "r")
c = open("c_medium.in", "r")
d = open("d_quite_big.in", "r")
e = open("e_also_big.in")


def donnees(fichier):
    txt = [line.split() for line in fichier]
    for i, x in enumerate(txt[1]):
        txt[1][i] = int(x)
    pizzas = txt[1]
    nbparts = int(txt[0][0])
    return pizzas, nbparts


def nb(pizzas, nbparts):
    n = len(pizzas)
    max = 0
    res = 0
    for i in range(n):
        for y in range(i):
            if res + pizzas[n - i - y] <= nbparts:
                res += pizzas[n - i - y]
        if res > max:
            max = res
        if max == nbparts:
            return max
    return max


pizzas, nbparts = donnees(a)

debut = time.time()
x = nb(pizzas, nbparts)
fin = time.time()
print("max:", nbparts)
print("res:", x)
print("diff:", abs(x - nbparts))
print("temps:", fin - debut)
