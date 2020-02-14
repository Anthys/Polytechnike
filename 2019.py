__author__ = 'julesmichaud'
__filename__ = '2019.py'
__date__ = '14/02/20'


def load(adr):
    f = open(adr, "r")
    txt = [line.split() for line in f]
    nb_photos = int(txt[0][0])
    photos = []
    for x in range(nb_photos):
        d = dict()
        indice = x
        typez = txt[x + 1][0]
        nb_arg = int(txt[x + 1][1])
        arg = set()
        for y in range(2, nb_arg + 2):
            arg.add(txt[x + 1][y])
        d["indice"] = indice
        d["type"] = typez
        d["nb_arg"] = nb_arg
        d["arg"] = arg
        photos.append(d)
    return photos


def dif_args(list_photo):
    args = []
    for i in list_photo:
        for j in i["arg"]:
            if not j in args:
                args += [j]

    return len(args)


def union(a,b):
    return a.union(b)


def inter(a,b):
    return a.intersection(b)


def difference(a,b):
    return a.difference(b)


def regroupe_V(liste):
    new_liste = []
    for indice in range(len(liste)):
        if indice < len(liste) - 5:
            max = 0
            for i in range(1, 6):
                a = min(difference(liste[indice], liste[indice+i]), difference(liste[indice+i], liste[indice]), inter(liste[indice], liste[indice+i]))
                if a > max:
                    max = a
        else :
            i_max = len(liste) - indice
            max = 0
            for i in range(1, i_max):



a = load("qualification_round_2019.in/e_shiny_selfies.txt")