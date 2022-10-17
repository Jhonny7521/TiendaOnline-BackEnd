from flask import Flask
from flask_cors import CORS

#Instanciamos la aplicación con Flask
app = Flask(__name__)
app.secret_key = "storeapp secret key"

# Establecemos las CORS para la comunicación de datos cruzados.
CORS(app, resources={r"/api/*": {"origins": "*"}})