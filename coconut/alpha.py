import Jules, Julien, Load

a = "a_example.txt"

file1 = open(a)
values, file1 = Load.load(file1)
b = Jules.tri_days_sign_up(file1)
Julien.print_output_file(b, values)