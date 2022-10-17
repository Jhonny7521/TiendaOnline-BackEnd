from flask import jsonify
from store_app import app
from store_app.models.product_model import Product

# Controlador con la ruta o Endpoint para obtener de todos los productos
@app.route("/api/products/")
def get_products():
  products = Product.get_all_products()
  return jsonify(products)

# Controlador con la ruta o Endpoint para la búsqueda de productos por categoría
@app.route("/api/products/category/<int:idCategory>")
def get_products_by_category(idCategory):

  data = {
    "category": idCategory
  }
  # data = (idCategory, )

  products = Product.get_products_by_category(data)
  return jsonify(products)

# Controlador con la ruta o Endpoint para la búsqueda de productos por texto ingresado
@app.route("/api/products/<string:text>")
def get_products_by_text(text):

  data = {
    "text": "%%"+ text + "%%"
  }

  products = Product.get_products_by_text(data)
  return jsonify(products)