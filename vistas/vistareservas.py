from flask_restful import Resource
from flask import request, jsonify
from marshmallow import ValidationError
from models import db, Reserva
from schemas import ReservaSchema

reserva_schema = ReservaSchema()
reservas_schema = ReservaSchema(many=True)

# Clase para manejar la creación y obtención de reservas con paginación
class VistaReservas(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        reservas = Reserva.query.paginate(page=page, per_page=per_page, error_out=False)
        return {
            "total": reservas.total,
            "pages": reservas.pages,
            "current_page": reservas.page,
            "reservas": reservas_schema.dump(reservas.items)
        }, 200

    def post(self):
        data = request.get_json()
        
        # Validación de datos
        try:
            nueva_reserva = reserva_schema.load(data)
        except ValidationError as err:
            return {"error": err.messages}, 400

        # Guardar la nueva reserva
        try:
            db.session.add(nueva_reserva)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"error": "Error al guardar la reserva", "details": str(e)}, 500
        
        return {"message": "Reserva creada con éxito", "data": reserva_schema.dump(nueva_reserva)}, 201

# Clase para manejar las operaciones sobre una reserva específica
class VistaReserva(Resource):
    def get(self, id):
        reserva = Reserva.query.get(id)
        if not reserva:
            return {"error": "Reserva no encontrada"}, 404
        return reserva_schema.dump(reserva), 200

    def put(self, id):
        reserva = Reserva.query.get(id)
        if not reserva:
            return {"error": "Reserva no encontrada"}, 404

        data = request.get_json()
        
        # Validación de datos
        try:
            updated_reserva = reserva_schema.load(data, partial=True)
        except ValidationError as err:
            return {"error": err.messages}, 400

        # Actualizar campos permitidos
        try:
            reserva.fecha = updated_reserva.get('fecha', reserva.fecha)
            reserva.hora = updated_reserva.get('hora', reserva.hora)
            reserva.usuario_cedula = updated_reserva.get('usuario_cedula', reserva.usuario_cedula)
            reserva.categoria_servicios = updated_reserva.get('categoria_servicios', reserva.categoria_servicios)
            
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"error": "Error al actualizar la reserva", "details": str(e)}, 500

        return {"message": "Reserva actualizada con éxito", "data": reserva_schema.dump(reserva)}, 200

    def delete(self, id):
        reserva = Reserva.query.get(id)
        if not reserva:
            return {"error": "Reserva no encontrada"}, 404
        
        try:
            db.session.delete(reserva)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"error": "Error al eliminar la reserva", "details": str(e)}, 500

        return {"message": "Reserva eliminada con éxito"}, 204
