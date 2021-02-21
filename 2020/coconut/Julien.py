import Load


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
  a.write(txt)

def tri_3(liste, values):
    liste.sort(key=lambda x: values[x], reverse=False)
    liste.reverse()
    return liste

def tri_nb_livres(liste):
    liste.sort(key=lambda x: (x["sum_score"] / (x["days_signup"] + x["books_per_day"] + len(x["books_ind"]))), reverse=True)
    return liste

def compter_points(liste_library, maxdays, books_score):
  books_done = [0]*len(books_score)
  day = 0
  points = 0
  for ind_library in range(len(liste_library)):
    #print(ind_library/len(liste_library)*100)
    print("NEW DAY, ", day, "/", maxdays)
    library = liste_library[ind_library]
    day += library['days_signup']
    if day > maxdays:
      break
    temp_day = day
    while temp_day < maxdays:
      #print(points)
      for j in range(library["books_per_day"]):
        if library['books_ind']:
          cur_ind = library["books_ind"][0]
          if books_done[cur_ind]==0:
            points += books_score[cur_ind]
            books_done[cur_ind]=1
          library["books_ind"].pop(0)
      temp_day += 1
  return points
        
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
    return books_score, Library, nb_days


def dicalyse(mes):
  temp = {"sum":0, "min":float("inf"), "max":-1, "mes":mes, "mean":0}
  return temp

def fill_dict(dictt, key, val):
  dictt[key]["sum"] += val
  if val > dictt[key]['max']:
    dictt[key]['max'] = val
  if val < dictt[key]['min']:
    dictt[key]['min'] = val
  return dictt

SUPERLISTE = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt","e_so_many_books.txt", "f_libraries_of_the_world.txt"]

def analyse(liste_library, values, name = "", max_days = 0):
  if name:
    print('\n')
    print("###", name, ":", "\n")
  fulldic = {}
  keys = ["signup", "books_lib", "points_libs", "books_val"]
  mes = ["Time to signup", "Number of books per libraries", "Sum_score per libraries", "Values of all books"]
  for k in range(len(keys)):
    val =keys[k]
    message = mes[k]
    fulldic[val] = dicalyse(message)

  for library in liste_library:
    fulldic = fill_dict(fulldic, "signup", library["days_signup"])
    fulldic = fill_dict(fulldic, "books_lib", len(library["books_ind"]))
    temp_sum = 0
    for book in library["books_ind"]:
      #print(book)
      temp_sum += values[book]
    fulldic = fill_dict(fulldic, "points_libs", temp_sum)
  for book in values:
    fulldic = fill_dict(fulldic, "books_val", book)

  fulldic["signup"]["mean"] = fulldic["signup"]["sum"]/len(liste_library)
  fulldic["books_lib"]["mean"] = fulldic["books_lib"]["sum"]/len(liste_library)
  fulldic["points_libs"]["mean"] = fulldic["points_libs"]["sum"]/len(liste_library)
  fulldic["books_val"]["mean"] = fulldic["books_val"]["sum"]/len(values)
  if False:
    for key in keys:
      cur_dic = fulldic[key]
      print(" ", cur_dic["mes"])
      print(" ", " ", "MAXIMUM:", cur_dic["max"])
      print(" ", " ", "MINIMUM:", cur_dic["min"])
      print(" ", " ", "MEAN:", cur_dic["mean"])
  else:
    print(" ", "Max days : ", max_days, "\n")
    print(" ", "Number of libraries : ", len(liste_library), "\n")
    print(" ", "Number of books : ", len(values), "\n")
    print()
    print("| | " + str(" | ".join(mes)) + " |")
    print("| --- | " + str(" | ".join(["---" for i in range(len(mes))])) + " |")
    maxs = [str(fulldic[key]["max"]) for key in keys]
    mins = [str(fulldic[key]["min"]) for key in keys]
    means = [str(fulldic[key]["mean"]) for key in keys]
    print("| **MAXIMUM** | " + str(" | ".join(maxs)) + " |")
    print("| **MINIMUM** | " + str(" | ".join(mins)) + " |")
    print("| **MEAN** | " + str(" | ".join(means)) + " |")
    if False:
      for key in keys:
        cur_dic = fulldic[key]
        print(" ", cur_dic["mes"])
        print(" ", " ", "MAXIMUM:", cur_dic["max"])
        print(" ", " ", "MINIMUM:", cur_dic["min"])
        print(" ", " ", "MEAN:", cur_dic["mean"])