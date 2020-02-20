import Load

a = open("a_example.txt", "r")


def tri_books(liste, books_score):
    for lib in liste:
        n = len(lib["books_ind"])
        for i in range(n - 1):
            maxim = i
            for j in range(i + 1, n):
                if books_score[lib["books_ind"][j]] > books_score[lib["books_ind"][maxim]]:
                    maxim = j
            if maxim != i:
                lib["books_ind"][i], lib["books_ind"][maxim] = lib["books_ind"][maxim], lib["books_ind"][i]
    return liste


def compute_sum_score(liste, scores):
    for libr in liste:
        sum = 0
        for book in libr["books_ind"]:
            sum += scores[book]
        libr["sum_score"] = sum
    return liste


def sum_score(library, scores):
    sum = 0
    for book in library["books_ind"]:
        sum += scores[book]
    return sum


def reorder_libraries(liste, scores):
    compute_sum_score(liste, scores)
    for i in range(len(liste) - 1):
        if liste[i + 1]["sum_score"] > liste[i]["sum_score"]:
            liste[i + 1], liste[i] = liste[i], liste[i + 1]
    return liste

