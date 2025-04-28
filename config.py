import pymysql
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

pymysql.install_as_MySQLdb()

# Inicialización de base de datos y migraciones
db = SQLAlchemy()
migrate = Migrate()

SECRET_KEY = 'examen_recurso'
