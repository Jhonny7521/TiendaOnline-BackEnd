from store_app.config.mysqlconnection import connectToMySQL

class Category:

  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
  
  @classmethod
  def get_all_categories(cls):
    query = "SELECT * FROM category;"
    results = connectToMySQL('bsale_test').query_db(query)
    return results
