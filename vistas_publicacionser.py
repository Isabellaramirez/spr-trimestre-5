from flask import Flask, jsonify, request, abort
from marshmallow import ValidationError
from models import db, Categoria_servicios 
from schemas import CategoriaServiciosSchema 

app = Flask(__name__)

servicio_schema = CategoriaServiciosSchema()
servicios_schema = CategoriaServiciosSchema(many=True)

# Publicar un nuevo servicio (POST)
@app.route('/servicios', methods=['POST'])
def create_servicio():
    data = request.get_json()

    # Validación de datos
    try:
        nuevo_servicio = servicio_schema.load(data, session=db.session)  
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Guardar el nuevo servicio
    db.session.add(nuevo_servicio)
    db.session.commit()
    
    return jsonify({"message": "Servicio publicado con éxito", "data": servicio_schema.dump(nuevo_servicio)}), 201

# Obtener todos los servicios (GET)
@app.route('/servicios', methods=['GET'])
def get_servicios():
    servicios = Categoria_servicios.query.all()
    return servicios_schema.jsonify(servicios), 200

# Obtener un servicio específico por ID (GET)
@app.route('/servicios/<int:id>', methods=['GET'])
def get_servicio(id):
    servicio = Categoria_servicios.query.get(id)
    if not servicio:
        return jsonify({"error": "Servicio no encontrado"}), 404
    return servicio_schema.jsonify(servicio), 200

# Actualizar un servicio (PUT)
@app.route('/servicios/<int:id>', methods=['PUT'])
def update_servicio(id):
    servicio = Categoria_servicios.query.get(id)
    if not servicio:
        return jsonify({"error": "Servicio no encontrado"}), 404

    data = request.get_json()

    # Validación de datos
    try:
        updated_servicio = servicio_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Actualizar campos permitidos
    servicio.nombre_categoria = updated_servicio.get('nombre_categoria', servicio.nombre_categoria)
    servicio.nombre_servicio = updated_servicio.get('nombre_servicio', servicio.nombre_servicio)

    db.session.commit()
    return jsonify({"message": "Servicio actualizado con éxito", "data": servicio_schema.dump(servicio)}), 200

# Eliminar un servicio (DELETE)
@app.route('/servicios/<int:id>', methods=['DELETE'])
def delete_servicio(id):
    servicio = Categoria_servicios.query.get(id)
    if not servicio:
        return jsonify({"error": "Servicio no encontrado"}), 404
    
    db.session.delete(servicio)
    db.session.commit()
    return jsonify({"message": "Servicio eliminado con éxito"}), 204
