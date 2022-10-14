from flask import jsonify
from store_app import app
from store_app.models.category_model import Category

@app.route("/api/category/")
def get_categories():
  categories = Category.get_all_categories()
  return jsonify(categories)