from flask import jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import db, Usuario, Producto, Categoria

# ------------------------- AUTENTICACIÓN -------------------------
def login_usuario(email, password):
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario and check_password_hash(usuario.password, password):
        token = create_access_token(identity=usuario.id)
        return {'access_token': token}, 200
    return {'msg': 'Credenciales incorrectas'}, 401

def registrar_usuario(nombre, email, password):
    if Usuario.query.filter_by(email=email).first():
        return {'msg': 'El usuario ya existe'}, 400
    nuevo_usuario = Usuario(nombre=nombre, email=email, password=generate_password_hash(password))
    db.session.add(nuevo_usuario)
    db.session.commit()
    return {'msg': 'Usuario registrado exitosamente'}, 201

# ------------------------- USUARIOS -------------------------
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return [u.to_dict() for u in usuarios], 200

def crear_usuario(nombre, email, password):
    nuevo_usuario = Usuario(nombre=nombre, email=email, password=generate_password_hash(password))
    db.session.add(nuevo_usuario)
    db.session.commit()
    return nuevo_usuario.to_dict(), 201

def actualizar_usuario(id, nombre=None, email=None, password=None):
    usuario = Usuario.query.get(id)
    if not usuario:
        return {'msg': 'Usuario no encontrado'}, 404
    if nombre:
        usuario.nombre = nombre
    if email:
        usuario.email = email
    if password:
        usuario.password = generate_password_hash(password)
    db.session.commit()
    return usuario.to_dict(), 200

def eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return {'msg': 'Usuario no encontrado'}, 404
    db.session.delete(usuario)
    db.session.commit()
    return {'msg': 'Usuario eliminado'}, 200

# ------------------------- PRODUCTOS -------------------------
def obtener_productos():
    productos = Producto.query.all()
    return [p.to_dict() for p in productos], 200

def crear_producto(nombre, precio, cantidad, categoria_id):
    nuevo_producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad, categoria_id=categoria_id)
    db.session.add(nuevo_producto)
    db.session.commit()
    return nuevo_producto.to_dict(), 201

def actualizar_producto(id, nombre=None, precio=None, cantidad=None, categoria_id=None):
    producto = Producto.query.get(id)
    if not producto:
        return {'msg': 'Producto no encontrado'}, 404
    if nombre:
        producto.nombre = nombre
    if precio is not None:
        producto.precio = precio
    if cantidad is not None:
        producto.cantidad = cantidad
    if categoria_id:
        producto.categoria_id = categoria_id
    db.session.commit()
    return producto.to_dict(), 200

def eliminar_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return {'msg': 'Producto no encontrado'}, 404
    db.session.delete(producto)
    db.session.commit()
    return {'msg': 'Producto eliminado'}, 200

# ------------------------- CATEGORÍAS -------------------------
def obtener_categorias():
    categorias = Categoria.query.all()
    return [c.to_dict() for c in categorias], 200

def crear_categoria(nombre):
    nueva_categoria = Categoria(nombre=nombre)
    db.session.add(nueva_categoria)
    db.session.commit()
    return nueva_categoria.to_dict(), 201

def actualizar_categoria(id, nombre=None):
    categoria = Categoria.query.get(id)
    if not categoria:
        return {'msg': 'Categoría no encontrada'}, 404
    if nombre:
        categoria.nombre = nombre
    db.session.commit()
    return categoria.to_dict(), 200

def eliminar_categoria(id):
    categoria = Categoria.query.get(id)
    if not categoria:
        return {'msg': 'Categoría no encontrada'}, 404
    db.session.delete(categoria)
    db.session.commit()
    return {'msg': 'Categoría eliminada'}, 200
