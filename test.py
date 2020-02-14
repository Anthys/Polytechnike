__author__ = "maxime"
__file__ = "test.py"
__date__ = "14/02/20"


def load(adr):
    f = open(adr, "r")
    txt = [line.split() for line in f]
    nb_photos = int(txt[0][0])
    photos = []
    for x in range(nb_photos):
        d = dict()
        indice = x
        type = txt[x + 1][0]
        nb_arg = int(txt[x + 1][1])
        arg = set()
        for y in range(2, nb_arg + 2):
            arg.add(txt[x + 1][y])
        d["indice"] = indice
        d["type"] = type
        d["nb_arg"] = nb_arg
        d["arg"] = arg
        photos.append(d)
    return photos
