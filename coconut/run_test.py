import Jules, Julien, Load, Sofiane, Maxime

a = "e_so_many_books.txt"

file1 = open(a)
values, file1 = Load.load(file1)
b = Jules.tri_1(file1)
list_lib = Sofiane.remove_multiple_occurrencies(b, values)
list_lib = Maxime.reorder_libraries(list_lib, values, Jules.tri_1)
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
Julien.print_output_file(b, values)