from store_app.config.mysqlconnection import connectToMySQL

class Product:

  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.url_image = data['url_image']
    self.price = data['price']
    self.discount = data['discount']
    self.category = data['category']
  
  @classmethod
  def get_all_products(cls):
    query = "SELECT * FROM product;"
    results = connectToMySQL('bsale_test').query_db(query)
    print(results)
    return results
  
  @classmethod
  def get_products_by_category(cls, data):
    print(data)
    query = "SELECT * FROM product WHERE category = %(category)s;"
    results = connectToMySQL('bsale_test').query_db(query,data)
    return results

  @classmethod
  def get_products_by_text(cls, data):
    print(data)
    query = 'SELECT * FROM product WHERE name LIKE %(text)s;'
    results = connectToMySQL('bsale_test').query_db(query, data)
    return results