from flask import Flask, jsonify, request, abort
from marshmallow import ValidationError
from models import db, Reserva  
from schemas import ReservaSchema  

app = Flask(__name__)

reserva_schema = ReservaSchema()
reservas_schema = ReservaSchema(many=True)

# Crear una reserva 
@app.route('/reservas', methods=['POST'])
def create_reserva():
    data = request.get_json()
    
    # Validación de datos
    try:
        nueva_reserva = reserva_schema.load(data)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Guardar la nueva reserva
    try:
        db.session.add(nueva_reserva)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al guardar la reserva", "details": str(e)}), 500
    
    return jsonify({"message": "Reserva creada con éxito", "data": reserva_schema.dump(nueva_reserva)}), 201

# Obtener todas las reservas con paginación
@app.route('/reservas', methods=['GET'])
def get_reservas():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    reservas = Reserva.query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        "total": reservas.total,
        "pages": reservas.pages,
        "current_page": reservas.page,
        "reservas": reservas_schema.dump(reservas.items)
    }), 200

# Obtener una reserva por ID 
@app.route('/reservas/<int:id>', methods=['GET'])
def get_reserva(id):
    reserva = Reserva.query.get(id)
    if not reserva:
        return jsonify({"error": "Reserva no encontrada"}), 404
    return jsonify(reserva_schema.dump(reserva)), 200

# Actualizar una reserva 
@app.route('/reservas/<int:id>', methods=['PUT'])
def update_reserva(id):
    reserva = Reserva.query.get(id)
    if not reserva:
        return jsonify({"error": "Reserva no encontrada"}), 404

    data = request.get_json()
    
    # Validación de datos
    try:
        updated_reserva = reserva_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Actualizar campos permitidos
    try:
        reserva.fecha = updated_reserva.get('fecha', reserva.fecha)
        reserva.hora = updated_reserva.get('hora', reserva.hora)
        reserva.usuario_cedula = updated_reserva.get('usuario_cedula', reserva.usuario_cedula)
        reserva.categoria_servicios = updated_reserva.get('categoria_servicios', reserva.categoria_servicios)

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar la reserva", "details": str(e)}), 500

    return jsonify({"message": "Reserva actualizada con éxito", "data": reserva_schema.dump(reserva)}), 200

# Eliminar una reserva 
@app.route('/reservas/<int:id>', methods=['DELETE'])
def delete_reserva(id):
    reserva = Reserva.query.get(id)
    if not reserva:
        return jsonify({"error": "Reserva no encontrada"}), 404
    
    try:
        db.session.delete(reserva)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar la reserva", "details": str(e)}), 500

    return jsonify({"message": "Reserva eliminada con éxito"}), 204
