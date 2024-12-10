import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./registrarse.css";

function Registrarse() {
  const [rol, setRol] = useState(""); // Estado para manejar el rol seleccionado
  const navigate = useNavigate();

  function handleSubmit(event) {
    event.preventDefault();

    // Crea un objeto FormData para manejar datos y archivos
    const formData = new FormData(event.target);

    // Imprime los datos enviados para depuración
    console.log("Datos enviados al servidor:");
    for (let pair of formData.entries()) {
      console.log(`${pair[0]}: ${pair[1]}`);
    }

    // Enviar los datos al servidor con Axios
    axios
      .post("http://localhost:3000/signin", formData, {
        headers: {
          "Content-Type": "multipart/form-data", // Este encabezado lo maneja Axios automáticamente
        },
      })
      .then((response) => {
        console.log("Respuesta del servidor:", response.data);
        // Redirigir al usuario a la página de inicio de sesión
        navigate("/iniciar-sesion");
      })
      .catch((error) => {
        console.error("Error al registrar el usuario:", error.response?.data || error.message);
        alert("Hubo un error al procesar tu solicitud. Revisa los datos ingresados.");
      });
  }

  function handleCancel() {
    navigate("/"); // Redirige al usuario a la página de inicio u otra que desees
  }

  return (
    <div>
      <h1>Gestión de Perfil</h1>
      <form onSubmit={handleSubmit}>
        {/* Selección de Rol */}
        <label>
          Rol:
          <select
            name="id_rol" // Asegúrate de que coincida con lo esperado en el backend
            value={rol}
            onChange={(e) => setRol(e.target.value)}
            required
          >
            <option value="">Selecciona un rol</option>
            <option value="1">Prestador de Servicios</option> {/* ID según el backend */}
            <option value="2">Contratista</option> {/* ID según el backend */}
          </select>
        </label>

        {/* Campos comunes para ambos roles */}
        <label>
          Cédula:
          <input type="text" name="cedula" required />
        </label>

        <label>
          Nombres:
          <input type="text" name="nombres" required />
        </label>

        <label>
          Apellidos:
          <input type="text" name="apellidos" required />
        </label>

        <label>
          Celular:
          <input type="text" name="celular" required />
        </label>

        <label>
          Dirección:
          <input type="text" name="direccion" required />
        </label>

        <label>
          Contraseña:
          <input type="password" name="contrasena" required />
        </label>

        <label>
          Correo:
          <input type="email" name="correo" required />
        </label>

        <label>
          Fecha de Nacimiento:
          <input type="date" name="fecha_nacimiento" required />
        </label>

        <label>
          Foto:
          <input type="file" name="foto" />
        </label>

        {/* Formulario para Prestador de Servicios */}
        {rol === "1" && (
          <>
            <label>
              Títulos Universitarios:
              <input type="text" name="titulos_uni" />
            </label>

            <label>
              Descripción:
              <textarea name="descripcion"></textarea>
            </label>
          </>
        )}

        {/* Formulario para Contratista */}
        {rol === "2" && (
          <label>
            Descripción:
            <textarea name="descripcion"></textarea>
          </label>
        )}

        <button type="submit">Registrarse</button>
        <button type="button" onClick={handleCancel} className="cancel-button">
          Cancelar
        </button>
      </form>
    </div>
  );
}

export default Registrarse;
