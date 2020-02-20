__author__ = 'julesmichaud'
__filename__ = 'delta.py.py'
__date__ = '20/02/20'

import Jules, Julien, Load

a = "a_example.txt"

file1 = open(a)
values, file1 = Load.load(file1)
b = Jules.tri_2(file1)
Julien.print_output_file(b, values)