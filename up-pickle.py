# Membuat graphnya
def make_graph (data) :
  Graph = {}
  daftar = data['Parent'].drop_duplicates()
  for i in daftar :
    Graph[i]=[]
  for i in range(len(data)) :
    a = [data['Child'][i],data['Heu'][i]]
    Graph[data['Parent'][i]].append(a)
  return Graph

# Mencari node yang mengandung nilai heu minimum
def find_min(graph):
  import pandas as pd
  Parent_min_heu = 'A'
  data = pd.DataFrame(graph,columns=['Parent','Heu'])
  min_heu = data['Heu'].min()
  for i in range(len(data)) :
    if (data['Heu'][i]==min_heu) :
      Parent_min_heu = data['Parent'][i]
  return Parent_min_heu

# Cek apakah node sudah pernah dikunjungi
def cek(Parent, path) :
  hasil = False
  if Parent in path :
    hasil = True
  return hasil

# Ambil nama nodenya saja
def ambil_Parent(graph) :
  import pandas as pd
  data = pd.DataFrame(graph,columns=['Parent','Heu'])
  Parents = data['Parent'].tolist()
  return Parents

# Mentidakaktifkan node yang pernah dikunjungi
def renew(active, path) :
  a = ambil_Parent(active)
  for i in range(len(a)) :
    b = cek(a[i],path)
    if b == True :
      active[i] = ['X',999]
  return active

# Mengaplikasikan algoritma greedy best first search
def gbfs(start,finish,graph):
  path = []
  visited = start
  path.append(visited)
  active = graph[start].copy()
  while visited != finish :
    active = renew(active,path)
    visited = find_min(active)
    path.append(visited)
    active = graph[visited].copy()
  return path

# Compile fungsi
def GreedyBestFirstSearch(start, finish, data) :
  list_node = data['Parent'].tolist()
  if (start in list_node) and (finish in list_node) :
    Graph = make_graph(data)
    Path = gbfs(start,finish,Graph)
    return Path
  else : 
    print("Node start dan / atau finish tidak ditemukan")