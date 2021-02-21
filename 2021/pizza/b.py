def suppression(tree, val):
   if val == tree.val:
      tree = suppression_racine(tree)
   elif val < tree.val:
      if tree.fils_gauche != None:
         tree.fils_gauche = suppression(tree.fils_gauche, val)
   elif val > tree.val:
      if tree.fils_droit != None:
         tree.fils_droit = suppression(tree.fils_droit, val)
    return tree

def suppression_racine(tree):
    if tree.fils_droit == None:
        tree = tree.fils_gauche
    else:
        tree1 = tree
        tree2 = tree.fils_droit
        if tree2.fils_droit == None:
            tree.val = tree2.val
            tree.fils_droit = tree2.fils_droit
        else:
            while tree2.fils_gauche != None:
                # Descente jusqu'au noeud le plus faible du s-a droit
                tree1 = tree2
                tree2 = tree2.fils_gauche
            tree.val = tree2.val
            tree1.filsgauche = tree2.fils_droit
    return tree