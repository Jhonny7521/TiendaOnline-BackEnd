from store_app.config.mysqlconnection import connectToMySQL

# ORM de la tabla Category
class Category:

  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
  
  # Método para enviár consulta a la base de datos y obtener todas las categorías.
  @classmethod
  def get_all_categories(cls):
    query = "SELECT * FROM category;"
    results = connectToMySQL('bsale_test').query_db(query)
    return results
