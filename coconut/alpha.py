import Jules, Julien, Load

a = "b_read_on.txt"

file1 = open(a)
book_scores, file1, maxdays = Julien.load(file1)
b = Jules.tri_days_sign_up(file1)
print(Julien.compter_points(b, maxdays, book_scores))
#Julien.print_output_file(b, book_scores)