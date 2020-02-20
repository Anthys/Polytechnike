import Jules, Julien, Load, Maxime

def remove_multiple_occurrencies(listoflibraries, books_score):
    Dict = dict()
    for i in range(len(books_score)):
        Dict[i] = False
    for library in listoflibraries:
        for element in library["books_ind"]:
            if Dict[element]:
                library["books_ind"].remove(element)
            Dict[element] = True
    return listoflibraries

L = [[1, 2, 4], [0, 2, 4]] #, [0, 0, 0, 0, 0], [1, 3, 4]]
H = []
for i in L:
    H += [{"books_ind":i}]
print(remove_multiple_occurrencies(H, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))


"""
#a = "a_example.txt"

file1 = open(a)
values, file1 = Load.load(file1)
b = Jules.tri_days_sign_up(file1)
c = Maxime.tri_books(b, values)

Julien.print_output_file(b, values)"""

