#serializacion 
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flaskr.modelos.modelos import Rol, Usuario, Categoria_servicios, Portafolio, Reserva, Historial, Estado_servicio, Mensajeria, Calificacion 




class EnumDicionario(fields.Field):  
    def _serialize(self, value, attr, obj, **kwargs):  
        if value is None:
            return None
        return {"llave": value.name, "valor": value.value}


class RolSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Rol 
        include_relationships = True
        load_instance = True

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

class CategoriaServiciosSchema(SQLAlchemyAutoSchema):  
    class Meta:
        model = Categoria_servicios
        include_relationships = True
        load_instance = True

class PortafolioSchema(SQLAlchemyAutoSchema):  
    class Meta:
        model = Portafolio
        include_relationships = True
        load_instance = True

class ReservaSchema(SQLAlchemyAutoSchema):  
    class Meta:
        model = Reserva
        include_relationships = True
        load_instance = True

class HistorialSchema(SQLAlchemyAutoSchema):  
    class Meta:
        model = Historial
        include_relationships = True
        load_instance = True

class EstadoServicioSchema(SQLAlchemyAutoSchema):  
    class Meta:
        model = Estado_servicio
        include_relationships = True
        load_instance = True

class MensajeriaSchema(SQLAlchemyAutoSchema):  
    class Meta:
        model = Mensajeria
        include_relationships = True
        load_instance = True


class CalificacionSchema(SQLAlchemyAutoSchema):  
    class Meta:
        model = Calificacion
        include_relationships = True
        load_instance = True