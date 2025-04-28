from flask import Blueprint, request, jsonify
from flasgger import swag_from
import controllers.controllers as controllers

routes = Blueprint('routes', __name__)

# ------------------------- RUTA PRINCIPAL -------------------------
@routes.route('/')
def index():
    return "API de gestión de usuarios, productos y categorías"

# ------------------------- AUTENTICACIÓN -------------------------
@routes.route('/login', methods=['POST'])
@swag_from({
    'summary': 'Inicio de sesión de usuario',
    'description': 'Permite a un usuario iniciar sesión con su email y contraseña.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {
                        'type': 'string',
                        'example': 'usuario@correo.com'
                    },
                    'password': {
                        'type': 'string',
                        'example': 'password123'
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Inicio de sesión exitoso',
            'schema': {
                'type': 'object',
                'properties': {
                    'token': {
                        'type': 'string',
                        'example': 'jwt_token_aqui'
                    }
                }
            }
        },
        '400': {
            'description': 'Error en el inicio de sesión'
        }
    }
})
def login():
    data = request.get_json()
    response, status = controllers.login_usuario(
        data.get('email'),
        data.get('password')
    )
    return jsonify(response), status

@routes.route('/registrar', methods=['POST'])
@swag_from({
    'summary': 'Registro de un nuevo usuario',
    'description': 'Permite registrar un nuevo usuario en la plataforma.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {
                        'type': 'string',
                        'example': 'Juan Pérez'
                    },
                    'email': {
                        'type': 'string',
                        'example': 'juan@correo.com'
                    },
                    'password': {
                        'type': 'string',
                        'example': 'contraseña123'
                    }
                }
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Usuario registrado con éxito'
        },
        '400': {
            'description': 'Error en el registro del usuario'
        }
    }
})
def registrar():
    data = request.get_json()
    response, status = controllers.registrar_usuario(
        data.get('nombre'),
        data.get('email'),
        data.get('password')
    )
    return jsonify(response), status

# ------------------------- USUARIOS -------------------------
@routes.route('/usuarios', methods=['GET'])
@swag_from({
    'summary': 'Obtener lista de usuarios',
    'description': 'Devuelve todos los usuarios registrados.',
    'responses': {
        '200': {
            'description': 'Lista de usuarios obtenida correctamente',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'example': 1
                        },
                        'nombre': {
                            'type': 'string',
                            'example': 'Juan Pérez'
                        },
                        'email': {
                            'type': 'string',
                            'example': 'juan@correo.com'
                        }
                    }
                }
            }
        },
        '400': {
            'description': 'Error al obtener usuarios'
        }
    }
})
def obtener_usuarios():
    response, status = controllers.obtener_usuarios()
    return jsonify(response), status

@routes.route('/usuarios', methods=['POST'])
@swag_from({
    'summary': 'Crear un nuevo usuario',
    'description': 'Permite crear un nuevo usuario en la plataforma.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {
                        'type': 'string',
                        'example': 'Juan Pérez'
                    },
                    'email': {
                        'type': 'string',
                        'example': 'juan@correo.com'
                    },
                    'password': {
                        'type': 'string',
                        'example': 'contraseña123'
                    }
                }
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Usuario creado exitosamente'
        },
        '400': {
            'description': 'Error al crear usuario'
        }
    }
})
def crear_usuario():
    data = request.get_json()
    response, status = controllers.crear_usuario(
        data.get('nombre'),
        data.get('email'),
        data.get('password')
    )
    return jsonify(response), status

@routes.route('/usuarios/<int:id>', methods=['PUT'])
@swag_from({
    'summary': 'Actualizar datos de un usuario',
    'description': 'Permite actualizar la información de un usuario existente.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'example': 1
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {
                        'type': 'string',
                        'example': 'Juan Pérez'
                    },
                    'email': {
                        'type': 'string',
                        'example': 'juan@correo.com'
                    },
                    'password': {
                        'type': 'string',
                        'example': 'contraseña123'
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Usuario actualizado exitosamente'
        },
        '400': {
            'description': 'Error al actualizar el usuario'
        }
    }
})
def actualizar_usuario(id):
    data = request.get_json()
    response, status = controllers.actualizar_usuario(
        id,
        data.get('nombre'),
        data.get('email'),
        data.get('password')
    )
    return jsonify(response), status

@routes.route('/usuarios/<int:id>', methods=['DELETE'])
@swag_from({
    'summary': 'Eliminar un usuario',
    'description': 'Permite eliminar un usuario de la plataforma.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'example': 1
        }
    ],
    'responses': {
        '200': {
            'description': 'Usuario eliminado correctamente'
        },
        '400': {
            'description': 'Error al eliminar el usuario'
        }
    }
})
def eliminar_usuario(id):
    response, status = controllers.eliminar_usuario(id)
    return jsonify(response), status

# ------------------------- PRODUCTOS -------------------------
@routes.route('/productos', methods=['GET'])
@swag_from({
    'summary': 'Obtener lista de productos',
    'description': 'Devuelve todos los productos registrados en la plataforma.',
    'responses': {
        '200': {
            'description': 'Lista de productos obtenida correctamente',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'example': 1
                        },
                        'nombre': {
                            'type': 'string',
                            'example': 'Camiseta'
                        },
                        'precio': {
                            'type': 'number',
                            'format': 'float',
                            'example': 25.5
                        },
                        'cantidad': {
                            'type': 'integer',
                            'example': 100
                        },
                        'categoria_id': {
                            'type': 'integer',
                            'example': 2
                        }
                    }
                }
            }
        },
        '400': {
            'description': 'Error al obtener productos'
        }
    }
})
def obtener_productos():
    response, status = controllers.obtener_productos()
    return jsonify(response), status

@routes.route('/productos', methods=['POST'])
@swag_from({
    'summary': 'Crear un nuevo producto',
    'description': 'Permite crear un nuevo producto en la plataforma.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {
                        'type': 'string',
                        'example': 'Camiseta'
                    },
                    'precio': {
                        'type': 'number',
                        'format': 'float',
                        'example': 25.5
                    },
                    'cantidad': {
                        'type': 'integer',
                        'example': 100
                    },
                    'categoria_id': {
                        'type': 'integer',
                        'example': 2
                    }
                }
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Producto creado exitosamente'
        },
        '400': {
            'description': 'Error al crear producto'
        }
    }
})
def crear_producto():
    data = request.get_json()
    response, status = controllers.crear_producto(
        data.get('nombre'),
        data.get('precio'),
        data.get('cantidad'),
        data.get('categoria_id')
    )
    return jsonify(response), status

@routes.route('/productos/<int:id>', methods=['PUT'])
@swag_from({
    'summary': 'Actualizar datos de un producto',
    'description': 'Permite actualizar la información de un producto existente.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'example': 1
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {
                        'type': 'string',
                        'example': 'Camiseta'
                    },
                    'precio': {
                        'type': 'number',
                        'format': 'float',
                        'example': 30.0
                    },
                    'cantidad': {
                        'type': 'integer',
                        'example': 120
                    },
                    'categoria_id': {
                        'type': 'integer',
                        'example': 2
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Producto actualizado exitosamente'
        },
        '400': {
            'description': 'Error al actualizar producto'
        }
    }
})
def actualizar_producto(id):
    data = request.get_json()
    response, status = controllers.actualizar_producto(
        id,
        data.get('nombre'),
        data.get('precio'),
        data.get('cantidad'),
        data.get('categoria_id')
    )
    return jsonify(response), status

@routes.route('/productos/<int:id>', methods=['DELETE'])
@swag_from({
    'summary': 'Eliminar un producto',
    'description': 'Permite eliminar un producto de la plataforma.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'example': 1
        }
    ],
    'responses': {
        '200': {
            'description': 'Producto eliminado correctamente'
        },
        '400': {
            'description': 'Error al eliminar el producto'
        }
    }
})
def eliminar_producto(id):
    response, status = controllers.eliminar_producto(id)
    return jsonify(response), status

# ------------------------- CATEGORÍAS -------------------------
@routes.route('/categorias', methods=['GET'])
@swag_from({
    'summary': 'Obtener lista de categorías',
    'description': 'Devuelve todas las categorías disponibles en la plataforma.',
    'responses': {
        '200': {
            'description': 'Lista de categorías obtenida correctamente',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'example': 1
                        },
                        'nombre': {
                            'type': 'string',
                            'example': 'Ropa'
                        }
                    }
                }
            }
        },
        '400': {
            'description': 'Error al obtener categorías'
        }
    }
})
def obtener_categorias():
    response, status = controllers.obtener_categorias()
    return jsonify(response), status

@routes.route('/categorias', methods=['POST'])
@swag_from({
    'summary': 'Crear una nueva categoría',
    'description': 'Permite crear una nueva categoría para los productos.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {
                        'type': 'string',
                        'example': 'Ropa'
                    }
                }
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Categoría creada exitosamente'
        },
        '400': {
            'description': 'Error al crear categoría'
        }
    }
})
def crear_categoria():
    data = request.get_json()
    response, status = controllers.crear_categoria(
        data.get('nombre')
    )
    return jsonify(response), status

@routes.route('/categorias/<int:id>', methods=['PUT'])
@swag_from({
    'summary': 'Actualizar datos de una categoría',
    'description': 'Permite actualizar la información de una categoría existente.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'example': 1
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {
                        'type': 'string',
                        'example': 'Electrónica'
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Categoría actualizada exitosamente'
        },
        '400': {
            'description': 'Error al actualizar categoría'
        }
    }
})
def actualizar_categoria(id):
    data = request.get_json()
    response, status = controllers.actualizar_categoria(
        id,
        data.get('nombre')
    )
    return jsonify(response), status

@routes.route('/categorias/<int:id>', methods=['DELETE'])
@swag_from({
    'summary': 'Eliminar una categoría',
    'description': 'Permite eliminar una categoría de la plataforma.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'example': 1
        }
    ],
    'responses': {
        '200': {
            'description': 'Categoría eliminada correctamente'
        },
        '400': {
            'description': 'Error al eliminar la categoría'
        }
    }
})
def eliminar_categoria(id):
    response, status = controllers.eliminar_categoria(id)
    return jsonify(response), status
