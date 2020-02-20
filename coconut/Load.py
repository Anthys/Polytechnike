__author__ = "maxime"
__file__ = "Load.py"
__date__ = "20/02/2020"

a = open("a_example.txt", "r")
b = open("b_read_on.txt")

def load(fichier):
    txt = [line.split() for line in fichier]
    nb_library = int(txt[0][1])
    nb_days = int(txt[0][2])
    books_score = []
    for x in txt[1]:
        books_score.append(int(x))

    Library = list()
    for i in range(nb_library):
        D = dict()
        D["books_per_day"] = int(txt[2 + 2 * i][2])
        D["days_signup"] = int(txt[2 + 2 * i][1])
        books_ind  = txt[3 + 2 * i]
        D["books_ind"] = []
        for x in books_ind:
            D["books_ind"].append(int(x))
        D["ind"] = i
        D["sum_score"] = 0
        for ind in D["books_ind"]:
            D["sum_score"] += books_score[ind]
        Library.append(D)
    return books_score, Library
