__author__ = "maxime"
__file__ = "georgelin_marc.py.py"
__date__ = "14/02/20"

import slide1 as sl
from charger_fichier import *


def tri_images(liste):
    liste.sort(key=lambda x: x["nb_arg"], reverse=True)


def ajoute_image(liste, new_im):
    argg = liste[0]["arg"]
    argd = liste[-1]["arg"]
    new_arg = new_im["arg"]

    Ig = len(sl.inter(argg, new_arg))
    Id = len(sl.inter(argd, new_arg))

    Dg = len(sl.difference(argg, new_arg))
    Dd = len(sl.difference(argd, new_arg))

    resg = min(Ig, Dg)
    resd = min(Id, Dd)

    if resg < resd:
        liste.append(new_im)
    else:
        liste = [new_im] + liste
    return liste, max(resg, resd)


def final(photos):
    diapo = []
    tri_images(photos)
    diapo.append(photos[0])
    del photos[0]

    res = 0
    for x in photos:
        diapo, c = ajoute_image(diapo, x)
        res += c

    return diapo, res


ph = load(b)
print(final(ph))
