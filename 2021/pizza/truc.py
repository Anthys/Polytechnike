import copy
def read_file(name):
    a = open(name, "r")
    lc = 0
    pizzas = []
    for l in a:
        if lc == 0:
            npizzas, nteams2, nteams3, nteams4 = [int(i) for i in l.split()]
        else:
            pizzas.append({'indice':lc-1, 'ing':l.split()[1:]})   
        lc +=1
    return npizzas, nteams2, nteams3, nteams4, pizzas

def minimal_intersect(pizzas, origset, istart=0, di=3):
    min_pizza = (istart, len(set(pizzas[istart]["ing"]).union(origset)) - 4.5*len(set(pizzas[istart]["ing"]).intersection(origset)))
    for i in range(istart+1, min(len(pizzas), istart + di)):
        l_inter = len(set(pizzas[i]["ing"]).union(origset)) - 4.5*len(set(pizzas[i]["ing"]).intersection(origset))
        if l_inter > min_pizza[1]:
            min_pizza = (i,l_inter)
    return min_pizza[0]

def minimal_intersect2(pizzas, origset, istart=0, di=3):
    min_pizza = (istart, len(set(pizzas[istart]["ing"]).intersection(origset)))
    for i in range(istart+1, min(len(pizzas), istart + di)):
        l_inter = len(set(pizzas[i]["ing"]).intersection(origset))
        if l_inter < min_pizza[1]:
            min_pizza = (i,l_inter)
    return min_pizza[0]

def retrieve_pizza(pizzas, i):
    return pizzas[:i] + pizzas[i+1:], pizzas[i]

def build_out(pizzas, nteams2, nteams3, nteams4):
    output = []
    teams_lists = [(4, nteams4), (3, nteams3), (2, nteams2)]
    for l_team_size in teams_lists:
        npiz   = l_team_size[0]
        nteams = l_team_size[1]
        for j in range(nteams):
            if len(pizzas) < npiz:
                break
            pizzas, init_pizza = retrieve_pizza(pizzas, 0)
            current_pizzas = [init_pizza["indice"]]
            current_ing_set = set(init_pizza["ing"])
            for k in range(npiz-1):
                #print(len(pizzas),minimal_intersect(pizzas, current_ing_set) )
                pizzas, best_pizz = retrieve_pizza(pizzas, minimal_intersect(pizzas, current_ing_set, 0,1000))
                current_pizzas.append(best_pizz["indice"])
                current_ing_set = current_ing_set.union(best_pizz["ing"])
            output.append(current_pizzas)
    return output

name = "c"
npizzas, nteams2, nteams3, nteams4, pizzas = read_file(name)
pizzas_originel = copy.deepcopy(pizzas)
#print(pizzas)

pizzas.sort(key= lambda i: len(i["ing"]), reverse=True)

output = build_out(pizzas, nteams2, nteams3, nteams4)
#print(output)

def nb_points(pizzas, output):
    assert (len(output) <= npizzas)
    nb_points, nb_teams2, nb_teams3, nb_teams4 = 0, 0, 0, 0
    for i in range(len(output)):
        ingredients = set()
        team_size = len(output[i])
        if team_size == 2: nb_teams2 += 1
        if team_size == 3: nb_teams3 += 1
        if team_size == 4: nb_teams4 += 1
        assert (nb_teams2 <= nteams2)
        assert (nb_teams3 <= nteams3)
        assert (nb_teams3 <= nteams3)
        for j in range(team_size):
            for ing in pizzas[output[i][j]]['ing'] :
                ingredients.add(ing)
        nb_points += len(ingredients) ** 2
    return nb_points

print(nb_points(pizzas_originel, output))

#print(len(set(pizzas[0]).intersection(set(pizzas[1]))))

def write_file(output, name="super.txt"):
    f = open(name, "w+")
    nb_tot = len(output)
    f.write(str(nb_tot))
    f.write("\n")
    for i in range(nb_tot):
        team = len(output[i])
        f.write(str(team))
        f.write(" ")
        for j in range(team):
            f.write(str(output[i][j]))
            f.write(" ")
        f.write("\n")
    f.close()

write_file(output, name+".out")