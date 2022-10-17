from store_app.config.mysqlconnection import connectToMySQL

# ORM de la tabla Products
class Product:

  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.url_image = data['url_image']
    self.price = data['price']
    self.discount = data['discount']
    self.category = data['category']
  
  # Método para enviár consulta a la base de datos y obtener todos los productos.
  @classmethod
  def get_all_products(cls):
    query = "SELECT * FROM product;"
    results = connectToMySQL('bsale_test').query_db(query)
    print(results)
    return results
  
  # Método para enviár consulta a la base de datos y obtener todos los productos según una categoría.
  @classmethod
  def get_products_by_category(cls, data):
    print(data)
    query = "SELECT * FROM product WHERE category = %(category)s;"
    results = connectToMySQL('bsale_test').query_db(query,data)
    return results

  # Método para enviár consulta a la base de datos y obtener todos los productos según un texto enviado.
  @classmethod
  def get_products_by_text(cls, data):
    print(data)
    query = 'SELECT * FROM product WHERE name LIKE %(text)s;'
    results = connectToMySQL('bsale_test').query_db(query, data)
    return results