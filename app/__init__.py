from flask import Flask 
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from .modelo import db
from .vistas import VistaContratista,  Vista_Mensajeria, VistaLogin, VistaSignIn, VistaPrestador
from flask_jwt_extended import JWTManager
from flask_cors import CORS



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)
    db.init_app(app)
    Migrate(app,db)
    JWTManager(app)
    
    api = Api(app)

    #aqui van las rutas
    #api.add_resouce()
    api.add_resource(VistaPrestador, '/prestador/<int:cedula>')
    api.add_resource(VistaContratista, '/contratista/<int:cedula>')
    api.add_resource(VistaSignIn, '/signin')
    api.add_resource(VistaLogin, '/login')
    api.add_resource(Vista_Mensajeria, '/mensajes')
    
    return app