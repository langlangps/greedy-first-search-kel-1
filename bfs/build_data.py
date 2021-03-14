from geopy.distance import geodesic

def get_heuristics_data(finish):
  data_with_coordinate = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/best first search project/data/data_with_coordinate.csv')
  route = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/best first search project/data/route.csv')
  row_finish = data_with_coordinate.query('nama_tempat == "{}"'.format(finish))

  def get_heuristics(node):
    row_start = data_with_coordinate.query('nama_tempat == "{}"'.format(node))
    return geodesic((row_start['latitude'].values, row_start['longitude'].values), (row_finish['latitude'].values, row_finish['longitude'].values)).km
  
  route['Heu'] = route.Child.apply(get_heuristics)

  return route.drop('Unnamed: 0', axis = 1)
  

data_with_coordinate = pd.read_csv('../data/data_with_coordinate.csv)
routes = pd.read_csv('../data/route.csv)