from flask import Flask
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy 
from marshmallow import fields
import enum 
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

app = Flask(__name__)



USER_DB = 'root'
PASS_DB = ''
URL_DB= 'localhost'
NAME_DB='spr'
FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'


app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


migrate = Migrate()
migrate.init_app(app, db)

Usuario_has_categoria_servicios = db.Table('Usuario_has_categoria_servicios',
    db.Column('cedula', db.Integer, db.ForeignKey('usuario.cedula'), primary_key=True),
    db.Column('id_categoria', db.Integer, db.ForeignKey('categoria_servicios.id_categoria'), primary_key=True)
)

Mensaje_x_porta = db.Table('Mensaje_x_porta',
    db.Column('id_portafolio', db.Integer, db.ForeignKey('portafolio.id_portafolio'), primary_key=True),
    db.Column('id_mensaje', db.Integer, db.ForeignKey('mensajeria.id_mensaje'), primary_key=True)
)

Usuario_x_calificacion = db.Table('Usuario_x_calificacion',
    db.Column('cedula', db.Integer, db.ForeignKey('usuario.cedula'), primary_key=True),
    db.Column('id_calificacion', db.Integer, db.ForeignKey('calificacion.id_calificacion'), primary_key=True)
)


class Rol(db.Model):
    id_rol = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(250))


    def __int__(self,id_rol,nombre_rol):
        self.id_rol = id_rol 
        self.nombre = nombre_rol

    def json(self):
        return {'id_rol': self.id_rol, 'nombre': self.nombre}

    def __str__(self):
        return str(self.__class__) + ": " + str (self.__dict__)



class Usuario(db.Model):
    cedula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    telfono = db.Column(db.String(250))
    direccion = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    correo = db.Column(db.String(250))
    fecha_nacimiento = db.Column(db.String(250))
    foto = db.Column(db.String(250))
    contraseña = db.Column(db.String(250))
    Categoria_servicios= db.relationship('Categoria_servicios',secondary= Usuario_has_categoria_servicios, back_populates='Usuario')
    Calificacion= db.relationship('Calificacion',secondary=Usuario_x_calificacion, back_populates='Usuario')
    Rol = db.Column(db.Integer, db.ForeignKey('rol.id_rol'))


    def __int__(self,cedula,nombre,apellido,telefono,direccion,correo,fecha_nacimiento,foto, contraseña):
        self.cedula = cedula
        self.nombre = nombre
        self.pellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.foto = foto
        self.contraseña = contraseña
    

    def json(self):
        return {'cedula': self.cedula,'nombre': self.nombre,'apellido': self.apellido,'telefono': self.telefono,'direccion': self.direccion,'correo': self.correo,'fecha_nacimiento': self.fecha_nacimiento,'foto': self.foto,'contraseña': self.contraseña}


    def __str__(self):
        return str(self.__class__) + ": " + str (self.__dict__)

class Categoria_servicios(db.Model):
    id_categoria = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(250))
    nombre_servicio = db.Column(db.String(250))
    Usuario= db.relationship('Usuario',secondary= Usuario_has_categoria_servicios, back_populates='Categoria_servicios')



    def __int__(self,id_categoria, nombre_categoria, nombre_servicio):
        self.id_categoria = id_categoria
        self.nombre_categoria = nombre_categoria
        self.nombre_servicio = nombre_servicio

    
    def json(self):
        return {'id_categoria': self.id_categoria, 'nombre_categoria': self.nombre_categoria, 'nombre_servicio': self.nombre_servicio}


    def __str__(self):
        return str(self.__class__) + ": " + str (self.__dict__)



class Portafolio(db.Model):
    id_portafolio = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(250))
    imagenes = db.Column(db.String(250))
    usuario_cedula = db.Column(db.Integer)
    Mensajeria= db.relationship('Mensajeria',secondary=Mensaje_x_porta, back_populates='Portafolio')
    Usuario = db.Column(db.Integer, db.ForeignKey('usuario.cedula'))
    


    def __int__(self,id_portafolio, descripcion, imagenes,usuario_cedula):
        self.id_portafolio = id_portafolio
        self.descripcion = descripcion
        self.imagenes = imagenes
        self.usuario_cedula = usuario_cedula

    
    def json(self):
        return {'id_portafolio': self.id_portafolio, 'descripcion': self.descripcion, 'imagenes': self.imagenes, 'usuario_cedula': self.usuario_cedula}


    def __str__(self):
        return str(self.__class__) + ": " + str (self.__dict__)


class Reserva (db.Model):
    id_reserva = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    hora = db.Column(db.String(250))
    usuario_cedula = db.Column(db.Integer)
    categoria_servicios = db.Column(db.Integer)
    Usuario = db.Column(db.Integer, db.ForeignKey('usuario.cedula'))
    Categoria_servicios = db.Column(db.Integer, db.ForeignKey('categoria_servicios.id_categoria'))

    def __int__(self,id_reserva, fecha, hora,usuario_cedula, categoria_servicios):
        self.id_reserva = id_reserva
        self.fecha = fecha
        self.hora = hora
        self.usuario_cedula = usuario_cedula


    def json(self):
        return {'id_reserva': self.id_reserva, 'fecha': self.fecha, 'hora': self.hora,'usuario_cedula': self.usuario_cedula,'categoria_servicios': self.categoria_servicios}


    def __str__(self):
        return str(self.__class__) + ": " + str (self.__dict__)


class Historial (db.Model):
    id_historial = db.Column(db.Integer, primary_key=True)
    reserva_id_reserva = db.Column(db.Integer)
    Reserva = db.Column(db.Integer, db.ForeignKey('reserva.id_reserva'))

    def __int__(self,id_historial, reserva_id_reserva):
        self.id_historial = id_historial
        self.reserva_id_reserva = reserva_id_reserva


    def json(self):
        return {'id_historial': self.id_historial, 'reserva_id_reserva': self.reserva_id_reserva, 'Reserva': self.reserva}


    def __str__(self):
        return str(self.__class__) + ": " + str (self.__dict__)

class Estado_servicio (db.Model):
    id_estado_servicio = db.Column(db.Integer, primary_key=True)
    estado_pago = db.Column(db.String(250))
    reporte = db.Column(db.String(250))
    reserva_id_reserva = db.Column(db.Integer)
    Reserva= db.Column(db.Integer, db.ForeignKey('reserva.id_reserva'))

    
    def __int__(self,id_estado_servicio, estado_pago,reporte,reserva_id_reserva):
        self.id_estado_servicio = id_estado_servicio
        self.estado_pago = estado_pago
        self.reporte = reporte
        self.reserva_id_reserva = reserva_id_reserva


    def json(self):
        return {'id_estado_servicio': self.id_estado_servicio, 'estado_pago': self.estado_pago, 'reporte': self.reporte,'reserva_id_reserva': self.reserva_id_reserva}

    
    def __str__(self):
        return str(self.__class__) + ": " + str (self.__dict__)




class Mensajeria(db.Model):
    id_mensaje = db.Column(db.Integer, primary_key=True)
    mensajes = db.Column(db.String(250))
    Portafolio= db.relationship('Portafolio',secondary=Mensaje_x_porta, back_populates='Mensajeria')

    def __init__(self, id_mensaje, mensajes): 
        self.id_mensaje = id_mensaje
        self.mensajes = mensajes

    def json(self):
        return {'id_mensaje': self.id_mensaje, 'mensajes': self.mensajes}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)






class Calificacion(db.Model):
    id_calificacion = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    Usuario= db.relationship('Usuario',secondary=Usuario_x_calificacion, back_populates='Calificacion')



    def __int__(self,id_calificacion, calificacion, descripcion):
        self.id_calificacion = id_calificacion
        self.calificacion = calificacion
        self.descripcion = descripcion


    def json(self):
        return {'id_calificacion': self.id_calificacion, 'calificacion': self.calificacion,'descripcion': self.descripcion }


    def __str__(self):
        return str(self.__class__) + ": " + str (self.__dict__)



class EnumDicionario(fields.Field):  # Cambié "filds.field" a "fields.Field"
    def _serialize(self, value, attr, obj, **kwargs):  # Cambié "def_serialize" a "_serialize"
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

