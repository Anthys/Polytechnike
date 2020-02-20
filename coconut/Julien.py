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
  print(txt)

def tri_3(liste, values):
    liste.sort(key=lambda x: values[x], reverse=False)
    liste.reverse()
    return liste