import Jules, Julien, Load, Maxime

def remove_multiple_occurrencies(listoflibraries, books_score):
    Dict = dict()
    for i in range(len(books_score)):
        Dict[i] = False
    j = 0
    for library in listoflibraries:
        
        # print(j)
        i = 0
        while i < len(library["books_ind"]):
            book_ind = library["books_ind"][i]
            #print(" ", str(library))
            if Dict[book_ind]:
                del library["books_ind"][i]
            else:
                i += 1
            Dict[book_ind] = True
        # print(" ",str(Dict))
        j += 1
    return listoflibraries
'''
L = [[1, 2, 4], [0, 4, 2]] #, [0, 0, 0, 0, 0], [1, 3, 4]]
H = []
for i in L:
    H += [{"books_ind":i}]
print(remove_multiple_occurrencies(H, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
'''
def remove_occurrencies_from_K(listoflibraries, books_score, K):
    Dict = dict()
    for i in range(len(books_score)):
        Dict[i] = False
    for library in listoflibraries[K:]:
        i = 0
        while i < len(library["books_ind"]):
            print(i)
            book_ind = library["books_ind"][i]
            print(" ", str(library))
            if Dict[book_ind]:
                del library["books_ind"][i]
            else:
                i += 1
            Dict[book_ind] = True
    return listoflibraries

L = [[1, 2, 4], [0, 4, 2], [0, 0, 0, 0, 0], [1, 3, 4]]
H = []
for i in L:
    H += [{"books_ind":i}]
print(remove_occurrencies_from_K(H, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 3))

'''
a = "a_example.txt"

file1 = open(a)
values, file1 = Load.load(file1)
b = Jules.tri_days_sign_up(file1)
c = Maxime.tri_books(b, values)

Julien.print_output_file(b, values)

'''