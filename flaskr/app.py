#app de flaskr
from flask import request
from flaskr import create_app
from .modelos import db
from flask_restful import Api, Resource
from .vistas.vistas_usuario import VistaUsuario, VistaUsuarioconsul
from .vistas.vista_mesajeria import Vista_Mensajeria
app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

api = Api(app)

api.add_resource(VistaUsuario, '/usuarios')

#editar y eliminar
api.add_resource(VistaUsuarioconsul, '/usuarios/<int:cedula>')

api.add_resource(Vista_Mensajeria, '/mensajeria')