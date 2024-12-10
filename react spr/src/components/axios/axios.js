import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Usuarios() {
  const [usuarios, setUsuarios] = useState([]);

  useEffect(() => {
    const fetchUsuarios = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/login'); // Reemplaza con la URL de tu endpoint
        setUsuarios(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchUsuarios();
  }, []);

  return (
    <div>
      {usuarios.map(usuario => (
        <div key={usuario.id}>
          {usuario.nombre}
        </div>
      ))}
    </div>
  );
}

export default Usuarios;