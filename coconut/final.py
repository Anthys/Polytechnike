a = "e_so_many_books.txt"

def tri_days_sign_up(liste):
    liste.sort(key=lambda x: x["days_signup"], reverse=False)
    return liste

def tri_1(liste):
    liste.sort(key=lambda x: (x["sum_score"] / (x["days_signup"] + x["books_per_day"])), reverse=True)
    return liste


def tri_2(liste):
    liste.sort(key=lambda x: (x["sum_score"] / (x["days_signup"]) - x["books_per_day"]), reverse=True)
    return liste

def print_output_file(liste_finale, values):
  txt = ""
  txt += str(len(liste_finale)) + "\n"
  for library in liste_finale:
    txt += str(library["ind"])
    txt += " "
    txt += str(len(library['books_ind']))
    txt += "\n"
    for book_ind in library['books_ind']:
      txt += str(book_ind) + " "
    txt += "\n"
  a = open("super", "w+")
  print(txt)

def tri_3(liste, values):
    liste.sort(key=lambda x: values[x], reverse=False)
    liste.reverse()
    return liste

def tri_nb_livres(liste):
    liste.sort(key=lambda x: (x["sum_score"] / (x["days_signup"] + x["books_per_day"] + len(x["books_ind"]))), reverse=True)
    return liste

def remove_occurrencies_from_K(listoflibraries, books_score, K):
    Dict = dict()
    for i in range(len(books_score)):#listoflibraries[K]["books_ind"]:
        Dict[i] = False
    for library in listoflibraries[K:]:
        i = 0
        while i < len(library["books_ind"]):
            book_ind = library["books_ind"][i]
            #print(" ", str(library))
            if Dict[book_ind]:
                del library["books_ind"][i]
            else:
                i += 1
            Dict[book_ind] = True
    return listoflibraries


def tri_books(liste, books_score):
    for lib in liste:
        n = len(lib["books_ind"])
        for i in range(n - 1):
            maxim = i
            for j in range(i + 1, n):
                if books_score[lib["books_ind"][j]] > books_score[lib["books_ind"][maxim]]:
                    maxim = j
            if maxim != i:
                lib["books_ind"][i], lib["books_ind"][maxim] = lib["books_ind"][maxim], lib["books_ind"][i]
    return liste


def compute_sum_score(liste, scores):
    for libr in liste:
        sum = 0
        for book in libr["books_ind"]:
            sum += scores[book]
        libr["sum_score"] = sum
    return liste


def sum_score(library, scores):
    sum = 0
    for book in library["books_ind"]:
        sum += scores[book]
    return sum


def reorder_libraries(liste, scores, tri_func):
    compute_sum_score(liste, scores)
    tri_func(liste)
    return liste


def reorder_libraries_ind(liste, scores, tri_func, ind):
    compute_sum_score(liste, scores)
    liste = liste[:ind + 1] + tri_func(liste[ind:])
    return liste

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

def remove_multiple_occurrencies(listoflibraries, books_score):
    Dict = dict()
    for i in range(len(books_score)):
        Dict[i] = False
    j = 0
    for library in listoflibraries:
        
        # print(j)
        i = 0
        while i < len(library["books_ind"]):
            book_ind = library["books_ind"][i]
            #print(" ", str(library))
            if Dict[book_ind]:
                del library["books_ind"][i]
            else:
                i += 1
            Dict[book_ind] = True
        # print(" ",str(Dict))
        j += 1
    return listoflibraries


file1 = open(a)
values, file1 = load(file1)
letri = tri_nb_livres
b = letri(file1)
list_lib = remove_multiple_occurrencies(b, values)
list_lib = reorder_libraries(list_lib, values, letri)
b = list_lib
for library_ind in range(len(b)):
  temp = b[library_ind]["books_ind"]
  b[library_ind]["books_ind"] = tri_3(temp, values)
i = 0
while i < len(b):
  if len(b[i]["books_ind"]) == 0:
    del b[i]
  else:
    i += 1
print_output_file(b, values)