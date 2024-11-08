from flask_restful import Resource
from flask import request 
from ..modelos import db, Usuario, UsuarioSchema

usuario_schema = UsuarioSchema()

class VistaUsuario(Resource):
    def get(self):
        return [usuario_schema.dump(Usuario) for Usuario in Usuario.query.all()] #esto es para traer todo lo 
                                                                                 #insertado 
    def post(self):
        nuevo_usuario = Usuario(cedula=request.json['cedula'], \
                                nombres=request.json['nombres'], \
                                apellidos=request.json['apellidos'], \
                                celular=request.json['celular'], \
                                direccion=request.json['direccion'], \
                                contraseña=request.jsom['contraseña'], \
                                titulos_uni=request.json['titulos_uni'], \
                                descripcion=request.json['descripcion'], \
                                correo=request.json['correo'],
                                fecha_nacimiento=request.json['fecha_nacimiento'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return usuario_schema.dump(nuevo_usuario), 201
    
class VistaUsuarioconsul(Resource):
    def get(self, cedula):
        return usuario_schema.dump(Usuario.query.get_or_404(cedula))
    
    def put(self, cedula):
        usuario = Usuario.query.get_or_404(cedula)
        usuario.nombres = request.json.get('nombres', usuario.nombres)
        usuario.apellidos = request.json.get('apellidos', usuario.apellidos)
        usuario.celular = request.json.get('celular', usuario.celular)
        usuario.direccion = request.json.get('direccion', usuario.direccion)
        usuario.contraseña = request.json.get('contraseña', usuario.contraseña)
        usuario.titulos_uni = request.json.get('titulos_uni', usuario.titulos_uni)
        usuario.descripciom = request.json.get('descripcion', usuario.descripcion)
        usuario.correo = request.json.get('correo', usuario.correo)
        usuario.fecha_nacimiento = request.jeson.get('fecha_nacimiento', usuario.fecha_nacimiento)
        if not Usuario:
            return 'usuario no encontrado', 404
    def delete(self, cedula):
        usuario = Usuario.query.get_or_404(cedula)
        db.session.delete(usuario)
        db.session.commit()
        return '', 204


    

                                
                                


