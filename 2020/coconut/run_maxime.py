__author__ = "maxime"
__file__ = "run_maxime.py"
__date__ = "20/02/2020"

import Jules, Julien, Load, Maxime

f = "f_libraries_of_the_world.txt"

file1 = open(f)
values, file1 = Load.load(file1)
b = Jules.tri_days_sign_up(file1)
Maxime.tri_books(b, values)
Julien.print_output_file(b, values)
