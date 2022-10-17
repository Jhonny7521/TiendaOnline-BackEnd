from flask import jsonify
from store_app import app
from store_app.models.category_model import Category

# Controlador con la ruta o Endpoint para obtener todas las categorias de los productoss
@app.route("/api/categories/")
def get_categories():
  categories = Category.get_all_categories()
  return jsonify(categories)