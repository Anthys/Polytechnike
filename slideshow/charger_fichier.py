a = "a_example.txt"
b = "b_lovely_landscapes.txt"
c = "c_memorable_moments.txt"
d = "d_pet_pictures.txt"
e = "e_shiny_selfies.txt"


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
        d["typ"] = type
        d["nb_arg"] = nb_arg
        d["arg"] = arg
        photos.append(d)
    return photos


def liste_verticale(photos):
    res = []
    for d in photos:
        if d["typ"] == "V":
            res.append(d)
    return res


def trier_verticale(liste):
    liste.sort(key=lambda x: x["nb_arg"])
    return liste
