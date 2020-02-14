def dif_args(list_photo):
    args = []
    for i in list_photo:
        for j in i["args"]:
            if not j in args:
                args += [j]

    return len(args)


def union(a, b):
    return a.union(b)


def inter(a, b):
    return a.intersection(b)


def difference(a, b):
    return a.difference(b)

