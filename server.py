from store_app import app
from store_app.controllers import products_controller, category_controller

# inicializamos la aplicación
if __name__ == "__main__":
  app.run(debug = True)