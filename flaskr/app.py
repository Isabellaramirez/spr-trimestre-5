# Flask y extensiones relacionadas
from flaskr import create_app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


import enum

from flaskr.modelos.modelos import db
from flaskr.modelos.schemas import UsuarioSchema, RolSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()


db.init_app(app) 



migrate = Migrate(app, db)




