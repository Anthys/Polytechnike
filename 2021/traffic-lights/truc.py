def read_in(f):
  a = open(f)
  simulation_info = {}
  streets = []
  MatIntersections = []
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
      MatIntersections[iStart][iEnd] = current_index_list
    elif iline - simulation_info["n_streets"]-1 < simulation_info["n_cars"]:
      tmp = line.split()
      len_path = int(tmp[0])
      path = tmp[1:]
      trajets_voitures.append(path)
  return trajets_voitures, MatIntersections, streets, simulation_info
  
trajets_voitures, MatIntersections, streets, simulation_info = read_in("a.txt")

def printl(l):
  for i in l:
    print(i)
  print("##")

printl(trajets_voitures)
printl(MatIntersections)
printl(streets)
print(simulation_info)


