from flask import Flask
from config import db
from models import Usuario, Categoria, Producto

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Fosforo1@database-6.cybqc82y6rrn.us-east-1.rds.amazonaws.com:3306/recurso'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

@app.route('/')
def index():
    return "Bienvenido a la API"

if __name__ == "__main__":
    app.run(debug=True)  # Ejecuta la aplicación en modo debug
