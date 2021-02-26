def read_in(f):
  a = open(f)
  simulation_info = {}
  streets = []
  MatIntersections = []
  nom_index_streets= {}
  trajets_voitures = []

  for iline, line in enumerate(a):
    if iline == 0:
      tmp = line.split()
      simulation_info = {
        "simulation_duree": int(tmp[0]),
        "n_intersect" : int(tmp[1]),
        "n_streets": int(tmp[2]),
        "n_cars":int(tmp[3]),
        "points_by_car": int(tmp[4]),
        "n_feux": 0,
      }
      MatIntersections = [[-1 for i in range(simulation_info["n_intersect"])] for j in range(simulation_info["n_intersect"])]
    elif iline < simulation_info["n_streets"]+1:
      tmp = line.split()
      iStart = int(tmp[0])
      iEnd = int(tmp[1])
      nom = tmp[2]
      taille = int(tmp[3])
      current_index_list = len(streets)
      streets.append({
        "nom": nom,
        "taille": taille,
        "istart": iStart,
        "iend": iEnd,
      })
      nom_index_streets[nom] = current_index_list
      MatIntersections[iStart][iEnd] = current_index_list
    elif iline - simulation_info["n_streets"]-1 < simulation_info["n_cars"]:
      tmp = line.split()
      len_path = int(tmp[0])
      path = tmp[1:]
      trajets_voitures.append(path)
  return trajets_voitures, MatIntersections, streets, simulation_info, nom_index_streets


file_in = "c.txt"
trajets_voitures, MatIntersections, streets, simulation_info, nom_index_streets= read_in(file_in)

def printl(l):
  print("##")
  for i in l:
    print(i)
  print("##")
#printl(MatIntersections)
#printl(streets)

def index_route_from_to(from_, to_):
  return MatIntersections[from_][to_]

def naive_solution():
    feux_output = [[] for a in range(simulation_info["n_intersect"])]
    for i in range(simulation_info["n_intersect"]):
        for j in range(simulation_info["n_intersect"]):
            index = index_route_from_to(j, i)
            if index != -1 :
                simulation_info["n_feux"] += 1
                feux_output[i].append({"duree" : 1 , "street_index" : index})
    return feux_output

def get_times(list_of_index, densities):
  out_times = [0]*len(list_of_index)
  densities = [densities[i]["density"] for i in list_of_index]
  for i,v in enumerate(densities):
    if densities[i] == 0:
      out_times[i] = 0
    elif densities[i] != 0:
      out_times[i] = 1
  return out_times

def create_densities(): # Crée la liste densities qui lie les indices des streets à leur densité
    densities = []
    for i, street in enumerate(streets):
        compteur = 0
        nom = street["nom"]
        for trajet in trajets_voitures:
            if nom in trajet: compteur += 1
        densities.append({"indice": i, "density": compteur})
    return densities

import numpy as np

def taille_itineraire(itineraire):
    compteur = 0
    for nom_street in itineraire:
        indice_street = nom_index_streets[nom_street]
        compteur += streets[indice_street]["taille"]
    return compteur

def create_tailles_itineraires():
    tailles_itineraires = []
    for itineraire in trajets_voitures:
        taille = taille_itineraire(itineraire)
        tailles_itineraires.append(taille)
    return tailles_itineraires

tailles_itineraires = create_tailles_itineraires()

densities = create_densities()


def create_densities_list():
    densities_list = []
    for street in densities:
        densities_list.append(street["density"])
    return densities_list
densities_list = create_densities_list()
def create_densities2(densities): # Crée la liste densities2 qui lie les indices des streets à leur densité (en prenant en compte la taille du trajet)
    densities2 = []
    for i, street in enumerate(streets):
        compteur = 0
        nom = street["nom"]
        for trajet in trajets_voitures:
            if nom in trajet: 
                mean_tailles_itineraires = np.mean(tailles_itineraires)
                min_tailles_itineraires = np.min(tailles_itineraires)
                if min_tailles_itineraires <= len(trajet) <= mean_tailles_itineraires:
                  compteur += np.mean(densities_list)*(mean_tailles_itineraires-len(trajet))/(mean_tailles_itineraires-min_tailles_itineraires)
                else: compteur += 1
        densities2.append({"indice": i, "density": compteur})
    return densities2
densities = create_densities2(densities)

def ponder_solution(densities):
    feux_output = [[] for a in range(simulation_info["n_intersect"])]
    for i in range(simulation_info["n_intersect"]):
        for j in range(simulation_info["n_intersect"]):
            index = index_route_from_to(j, i)
            if index != -1 and densities[index]["density"]!=0:
                simulation_info["n_feux"] += 1
                feux_output[i].append({"duree" : 1 , "street_index" : index})
    return feux_output


def ponder_solution2(densities):
    feux_output = [[] for a in range(simulation_info["n_intersect"])]
    for i in range(simulation_info["n_intersect"]):
        list_of_index = []
        for j in range(simulation_info["n_intersect"]):
            index = index_route_from_to(j, i)
            if index != -1 and densities[index]["density"]!=0:
                #list_of_index += [{"i":index, "d": densities[index], "duree":0}]
                computed_time = min(densities[i]["density"], simulation_info["simulation_duree"]-1)
                feux_output[i].append({"duree" :  computed_time, "street_index" : index})
    return feux_output

def ponder_solution3(densities):
    feux_output = [[] for a in range(simulation_info["n_intersect"])]
    for i in range(simulation_info["n_intersect"]):
        list_of_routes = []
        for j in range(simulation_info["n_intersect"]):
            index = index_route_from_to(j, i)
            if index != -1 and densities[index]["density"]!=0:
              list_of_routes.append(index)
        sum_density = sum([densities[i]["density"] for i in list_of_routes])
        minimums = [densities[list_of_routes[i]]["density"]/sum_density for i in range(len(list_of_routes))]
        for j,index in enumerate(list_of_routes):
            computed_time = max(1,min(int(densities[j]["density"]), int(simulation_info["simulation_duree"]*minimums[j]-1)))
            feux_output[i].append({"duree" :  computed_time, "street_index" : index})
    return feux_output

def naive_solution():
    feux_output = [[] for a in range(simulation_info["n_intersect"])]
    for i in range(simulation_info["n_intersect"]):
        for j in range(simulation_info["n_intersect"]):
            index = index_route_from_to(j, i)
            if index != -1 :
                simulation_info["n_feux"] += 1
                feux_output[i].append({"duree" : 1 , "street_index" : index})
    return feux_output

feux_output = ponder_solution3(densities)
def output_file(f_name, feux_output):
    f = open(f_name, "w")
    nb_intersections = 0
    for i in range(simulation_info["n_intersect"]):
        if feux_output[i] != []:
            nb_intersections += 1
    f.write(str(nb_intersections))
    f.write("\n")
    for i in range(simulation_info["n_intersect"]):
        if feux_output != []:
            feux_intersections = feux_output[i]
            nb_street = len(feux_output[i])
            if nb_street == 0:
              continue
            f.write(str(i))
            f.write("\n")
            f.write(str(nb_street))
            f.write("\n")
            for j in range(nb_street):
                feu = feux_intersections[j]
                inom = feu["street_index"]
                route = streets[inom]
                f.write(route["nom"] + " ")
                f.write(str(feux_output[i][j]["duree"]))
                f.write("\n")


output_file(file_in+".out", feux_output)