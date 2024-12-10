import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './formulario_login.css';

function FormularioLogin() {
  // Estados
  const [correo, setCorreo] = useState('');
  const [contraseña, setContraseña] = useState('');
  const [rol, setRol] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate(); // Para redirigir

  // Manejar cambios en el campo de correo
  function handleCorreoChange(e) {
    setCorreo(e.target.value);
  }

  // Manejar cambios en el campo de contraseña
  function handleContraseñaChange(e) {
    setContraseña(e.target.value);
  }

  // Manejar cambios en el campo de rol
  function handleRolChange(e) {
    setRol(e.target.value);
  }

  // Manejar el envío del formulario
  function handleSubmit(e) {
    e.preventDefault();
    
    if (correo && contraseña && rol) {
      setError('');
      navigate('/'); // Redirigir al Home
    } else {
      setError('Por favor, complete todos los campos');
    }
  }

  return (
    <div className="contenedor-login">
      <h2 className="titulo-login">Iniciar Sesión</h2>
      {error && <div className="error-message">{error}</div>}

      <form className="formulario-login" onSubmit={handleSubmit}>
        {/* Selección del rol */}
        <select
          id="rol"
          name="rol"
          value={rol}
          onChange={handleRolChange}
          required
        >
          <option value="" disabled>--- Seleccionar Rol ---</option>
          <option value="contratista">Contratista</option>
          <option value="prestador">Prestador de servicios</option>
        </select>

        {/* Campo de correo */}
        <input
          type="email"
          id="correo"
          name="correo"
          placeholder="Correo"
          value={correo}
          onChange={handleCorreoChange}
          required
        />

        {/* Campo de contraseña */}
        <input
          type="password"
          id="contraseña"
          name="contraseña"
          placeholder="Contraseña"
          value={contraseña}
          onChange={handleContraseñaChange}
          required
        />

        {/* Botón de iniciar sesión */}
        <button type="submit">Iniciar Sesión</button>
      </form>
    </div>
  );
}

export default FormularioLogin;
