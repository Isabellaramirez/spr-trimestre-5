import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";
import "./perfilcontratista.css";

function PerfilContratista() {
  const { id } = useParams(); // Obtener el ID del contratista desde la URL
  const navigate = useNavigate();

  const [perfil, setPerfil] = useState({
    nombres: "",
    apellidos: "",
    celular: "",
    direccion: "",
    correo: "",
    descripcion: "",
  });
  const [isEditing, setIsEditing] = useState(false);

  // Obtener datos del contratista
  useEffect(() => {
    axios
      .get(`http://localhost:5000/contratista/<int:cedula>`)
      .then((response) => {
        setPerfil(response.data);
      })
      .catch((error) => {
        console.error("Error al obtener el perfil:", error);
      });
  }, [id]);

  // Manejar el cambio en el formulario
  const handleChange = (event) => {
    const { name, value } = event.target;
    setPerfil({ ...perfil, [name]: value });
  };

  // Actualizar perfil
  const handleUpdate = (event) => {
    event.preventDefault();
    axios
      .put(`http://localhost:5000/contratista/<int:cedula>`, perfil)
      .then((response) => {
        alert(response.data.message);
        setIsEditing(false);
      })
      .catch((error) => {
        console.error("Error al actualizar el perfil:", error);
      });
  };

  // Eliminar perfil
  const handleDelete = () => {
    if (window.confirm("¿Estás seguro de que quieres eliminar tu perfil?")) {
      axios
        .delete(`http://localhost:5000/contratista/<int:cedula>`)
        .then((response) => {
          alert(response.data.message);
          navigate("/"); // Redirigir a la página principal o donde lo desees
        })
        .catch((error) => {
          console.error("Error al eliminar el perfil:", error);
        });
    }
  };

  return (
    <div className="perfil-container">
      <h1>Perfil del Contratista</h1>

      {isEditing ? (
        <form onSubmit={handleUpdate} className="perfil-form">
          <label>
            Nombres:
            <input
              type="text"
              name="nombres"
              value={perfil.nombres}
              onChange={handleChange}
              required
            />
          </label>

          <label>
            Apellidos:
            <input
              type="text"
              name="apellidos"
              value={perfil.apellidos}
              onChange={handleChange}
              required
            />
          </label>

          <label>
            Celular:
            <input
              type="text"
              name="celular"
              value={perfil.celular}
              onChange={handleChange}
              required
            />
          </label>

          <label>
            Dirección:
            <input
              type="text"
              name="direccion"
              value={perfil.direccion}
              onChange={handleChange}
              required
            />
          </label>

          <label>
            Correo:
            <input
              type="email"
              name="correo"
              value={perfil.correo}
              onChange={handleChange}
              required
            />
          </label>

          <label>
            Descripción:
            <textarea
              name="descripcion"
              value={perfil.descripcion}
              onChange={handleChange}
            />
          </label>

          <button type="submit">Actualizar Perfil</button>
        </form>
      ) : (
        <div className="perfil-details">
          <p><strong>Nombres:</strong> {perfil.nombres}</p>
          <p><strong>Apellidos:</strong> {perfil.apellidos}</p>
          <p><strong>Celular:</strong> {perfil.celular}</p>
          <p><strong>Dirección:</strong> {perfil.direccion}</p>
          <p><strong>Correo:</strong> {perfil.correo}</p>
          <p><strong>Descripción:</strong> {perfil.descripcion}</p>

          <button onClick={() => setIsEditing(true)}>Editar Perfil</button>
          <button onClick={handleDelete} className="delete-button">Eliminar Perfil</button>
        </div>
      )}
    </div>
  );
}

export default PerfilContratista;
