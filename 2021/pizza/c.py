def generate_arbre(registre):
    if len(registre) == 2:
        tree1 = AMB(None, H(transaction2txt(registre[0])), None)
        tree2 = AMB(None, H(transaction2txt(registre[1])), None)
    else:
        r1 = registre[:len(registre)//2]
        r2 = registre[:len(registre)//2+1]
        tree1 = generate_arbre(r1)
        tree2 = generate_arbre(r2)
    hash0 = H(str(tree1.val) + str(tree2.val))
    return ABM(tree1, hash0, tree2)