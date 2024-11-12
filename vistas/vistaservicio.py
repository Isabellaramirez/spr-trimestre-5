from flask_restful import Resource
from flask import request, jsonify
from marshmallow import ValidationError
from models import db, Categoria_servicios
from schemas import CategoriaServiciosSchema

servicio_schema = CategoriaServiciosSchema()
servicios_schema = CategoriaServiciosSchema(many=True)

# Vista para manejar todos los servicios (GET y POST)
class VistaServicios(Resource):
    def get(self):
        servicios = Categoria_servicios.query.all()
        return servicios_schema.dump(servicios), 200
    
    def post(self):
        data = request.get_json()
        
        # Validación de datos
        try:
            nuevo_servicio = servicio_schema.load(data, session=db.session)
        except ValidationError as err:
            return {"error": err.messages}, 400
        
        # Guardar el nuevo servicio
        db.session.add(nuevo_servicio)
        db.session.commit()
        
        return {"message": "Servicio publicado con éxito", "data": servicio_schema.dump(nuevo_servicio)}, 201

# Vista para manejar un servicio específico por ID (GET, PUT y DELETE)
class VistaServicio(Resource):
    def get(self, id):
        servicio = Categoria_servicios.query.get_or_404(id)
        return servicio_schema.dump(servicio), 200
    
    def put(self, id):
        servicio = Categoria_servicios.query.get_or_404(id)
        data = request.get_json()
        
        # Validación de datos
        try:
            updated_servicio = servicio_schema.load(data, partial=True)
        except ValidationError as err:
            return {"error": err.messages}, 400

        # Actualizar campos permitidos
        servicio.nombre_categoria = data.get('nombre_categoria', servicio.nombre_categoria)
        servicio.nombre_servicio = data.get('nombre_servicio', servicio.nombre_servicio)
        
        db.session.commit()
        return {"message": "Servicio actualizado con éxito", "data": servicio_schema.dump(servicio)}, 200

    def delete(self, id):
        servicio = Categoria_servicios.query.get_or_404(id)
        db.session.delete(servicio)
        db.session.commit()
        return {"message": "Servicio eliminado con éxito"}, 204