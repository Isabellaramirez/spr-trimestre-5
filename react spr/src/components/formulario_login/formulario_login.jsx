import React from 'react';
import './formulario_login.css';
import logo from '../../assets/images/logo.png';

const FormularioLogin = () => {
    return (
        <div className="contenedor-login">
            {/* Título del formulario */}
            <h2 className="titulo-login">Iniciar Sesión</h2>

            {/* Imagen del logo */}
            <img src={logo} alt="Logo de la aplicación" className="logo" />

            {/* Formulario */}
            <form className="formulario-login">
                {/* Selección del rol */}
                <select id="rol" name="rol" required>
                    <option value="" disabled selected>--- Seleccionar Rol ---</option>
                    <option value="contratista">Contratista</option>
                    <option value="prestador">Prestador de servicios</option>
                </select>

                {/* Campos de correo y contraseña */}
                <input type="email" id="correo" name="correo" placeholder="Correo" required />
                <input type="password" id="contraseña" name="contraseña" placeholder="Contraseña" required />

                {/* Botón de inicio de sesión */}
                <button type="submit">Iniciar Sesión</button>
            </form>
        </div>
    );
};

export default FormularioLogin;