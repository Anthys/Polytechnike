import Jules, Julien, Load, Sofiane, Maxime

a = "d_tough_choices.txt"

file1 = open(a)
#values, file1 = Load.load(file1)
book_scores, file1, maxdays = Julien.load(file1)
for a in Julien.SUPERLISTE:
  file1 = open(a)
  #values, file1 = Load.load(file1)
  book_scores, file1, maxdays = Julien.load(file1)
  Julien.analyse(file1, book_scores, a, max_days= maxdays)