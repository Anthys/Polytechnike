__author__ = "maxime"
__file__ = "Load.py"
__date__ = "20/02/2020"

# bite
def load(fichier):
    txt = [line.split() for line in fichier]
    for i, x in enumerate(txt[1]):
        txt[1][i] = int(x)
    pizzas = txt[1]
    nbparts = int(txt[0][0])
    return pizzas, nbparts
