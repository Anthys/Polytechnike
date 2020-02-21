import Jules, Julien, Load, Sofiane, Maxime

a = "d_tough_choices.txt"

file1 = open(a)
#values, file1 = Load.load(file1)
book_scores, file1, maxdays = Julien.load(file1)
values = book_scores
letri = Jules.tri_2
b = letri(file1)
list_lib = Sofiane.remove_multiple_occurrencies(b, values)
list_lib = Maxime.reorder_libraries(list_lib, values, letri)
b = list_lib
for library_ind in range(len(b)):
  temp = b[library_ind]["books_ind"]
  b[library_ind]["books_ind"] = Julien.tri_3(temp, values)
i = 0
while i < len(b):
  if len(b[i]["books_ind"]) == 0:
    del b[i]
  else:
    i += 1
print(Julien.compter_points(b, maxdays, book_scores))
#Julien.print_output_file(b, values)