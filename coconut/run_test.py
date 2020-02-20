import Jules, Julien, Load

a = "f_libraries_of_the_world.txt"

file1 = open(a)
values, file1 = Load.load(file1)
b = Jules.tri_days_sign_up(file1)
for library_ind in range(len(b)):
  temp = b[library_ind]["books_ind"]
  b[library_ind]["books_ind"] = Julien.tri_3(temp, values)  
Julien.print_output_file(b, values)