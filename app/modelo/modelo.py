from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()



class Rol(db.Model):
    __tablename__='rol'
    id_rol = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(200))
    usuario = db.relationship('Usuario', uselist=False, backref='user') #crea la relacion uno a uno el uselist=flase asegura que sqlalchemy trate esta relacion como uno a uno y no como uno a muchos

    def __init__(self, id_rol, rol):
        self.id_rol = id_rol
        self.rol = rol

usuario_categoria = db.Table('usuario_categoria',
    db.Column('cedula', db.Integer, db.ForeignKey('usuario.cedula'), primary_key=True),
    db.Column('categoria_id', db.Integer, db.ForeignKey('categoria.id_categoria'), primary_key=True)
)

usuario_calificacion = db.Table('usuario_calificacion',
    db.Column('cedula', db.Integer, db.ForeignKey('usuario.cedula'), primary_key=True),
    db.Column('id_calificacion', db.Integer, db.ForeignKey('calificacion.id_calificacion'), primary_key=True)
    )

class Usuario(db.Model):
    __tablename__ = 'usuario'
    cedula = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(128))
    apellidos = db.Column(db.String(128))
    celular = db.Column(db.String(10))
    direccion = db.Column(db.String(300))
    contrasena_hash = db.Column(db.String(300))
    titulos_uni = db.Column(db.String(250))
    descripcion = db.Column(db.String(500))
    correo = db.Column(db.String(200))
    fecha_nacimiento = db.Column(db.Date)
    foto = db.Column(db.String(300))
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id_rol')) #aqui va a estar el id de la tabla rol
    portafolios = db.relationship('Portafolio', backref='usercategory')
    reservas = db.relationship('Reserva', backref = 'user_reserva')
    categorias = db.relationship('Categoria', secondary=usuario_categoria , backref='usuario')

    @property
    def contrasena(self):
        raise ArithmeticError("la contrasena no es un atributo legible")
    
    @contrasena.setter
    def contrasena(self, password):
        self.contrasena_hash = generate_password_hash(password)

    def verificar_contrasena(self, password):
        return check_password_hash(self.contrasena_hash, password)
    
    def __init__(self, cedula, nombres, apellidos, celular, direccion, contrasena, titulos_uni, descripcion, correo, fecha_nacimiento, foto):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.celular = celular
        self.direccion = direccion
        self.contrasena = contrasena
        self.titulos_uni = titulos_uni
        self.descripcion = descripcion
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.foto = foto

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id_categoria = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(250))
    nombre_servicio = db.Column(db.String(250))
    mensajeria= db.relationship('Mensajes', backref='categorias_mesage')

    def __init__(self, id_categoria, nombre_servicio):
        self.id_categoria = id_categoria
        self.nombre_servicio = nombre_servicio

class Mensajes(db.Model):
    id_mensaje = db.Column(db.Integer, primary_key=True)
    mensajes = db.Column(db.String(500))
    id_categorias = db.Column(db.Integer, db.ForeignKey('categoria.id_categoria'))

    def __init__(self, id_mensaje, mensajes):
        self.id_mensaje = id_mensaje
        self.mensajes = mensajes


class Portafolio(db.Model):
    __tablename__='portafolios'
    id_portafolio = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(128))
    imagenes = db.Column(db.String(300))
    usuario_cedula = db.Column(db.Integer, db.ForeignKey('usuario.cedula'))

    def __init__(self, id_portafolio, descripcion, imagenes):
        self.id_portafolio = id_portafolio
        self.descripcion = descripcion
        self.imagenes = imagenes

class Reserva(db.Model):
    __tablename__='reserva'
    id_reserva = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    usuario_cedula = db.Column(db.Integer, db.ForeignKey('usuario.cedula'))
    historial = db.relationship('Historial', uselist=False, backref= 'reservhis')
    estado_ser = db.relationship('Estado_ser', uselist=False, backref='reserva')

    def __init__(self,id_reserva, fecha, hora):
        self.id_reserva = id_reserva
        self.fecha = fecha
        self.hora = hora    

class Historial(db.Model):
    __tablename__='historial'
    id_historial = db.Column(db.Integer, primary_key=True)
    reservas = db.Column(db.Integer, db.ForeignKey('reserva.id_reserva'), unique=True) #el unique true es para asegurar que una reserva solo tenga un historial

    def __init__(self,id_historial):
        self.id_historial = id_historial

class Calificacion(db.Model):
    __tablename__='calificacion'
    id_calificacion = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.Integer)
    descripcion = db.Column(db.String(250))
    usuarios= db.relationship('Usuario', secondary=usuario_calificacion, backref='calificaciones')
    

class Estado_ser(db.Model):
    __tablename__='estado_servicios'
    id_estado = db.Column(db.Integer, primary_key=True)
    estado_pago = db.Column(db.String(128))
    reporte = db.Column(db.String(128))
    estado_reserva = db.Column(db.Integer, db.ForeignKey('reserva.id_reserva', ondelete="CASCADE"), unique=True)

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

class CategoriasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
        include_relationships = True
        load_instance = True
        
class MensajesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Mensajes
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

class Estado_serSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Estado_ser
        include_relationships = True
        load_instance = True

class CalificacionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Calificacion
        include_relationships = True
        load_instance = True