import React, { createContext, useState } from "react";

export const AutenticacionContexto = createContext();

const AutenticacionProveedor = ({ children }) => {
  const [usuario, setUsuario] = useState(null);

  const iniciarSesion = (correo, contrasena) => {
    // Simulación de autenticación
    if (correo === "usuario@ejemplo.com" && contrasena === "123456") {
      setUsuario({ correo });
      alert("Inicio de sesión exitoso");
    } else {
      alert("Credenciales incorrectas");
    }
  };

  return (
    <AutenticacionContexto.Provider value={{ usuario, iniciarSesion }}>
      {children}
    </AutenticacionContexto.Provider>
  );
};

export default AutenticacionProveedor;
