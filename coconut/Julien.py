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
    print(ind_library/len(liste_library)*100)
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
