from flask_restful import Resource
from flaskr.modelos import db, Mensajes, MensajesSchema
from flask import request

mensajes_schema = MensajesSchema


class Vista_Mensajeria(Resource):
    def get(self):
        return [mensajes_schema.dump(Mensajes) for Mensajes in Mensajes.query.all()]
    def post(self):
        nuevo_mensaje = Mensajes(mensajes=request.json['mensajes'])
        db.session.add(nuevo_mensaje)
        return mensajes_schema.dump(nuevo_mensaje), 201


