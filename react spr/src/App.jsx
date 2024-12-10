import React from "react";
import { BrowserRouter as Router, Route, Routes, Navigate } from "react-router-dom";
import Login from "./pages/login/login";
import AutenticacionProveedor from "./contexto/autenticacion_contexto";

const App = () => {
  return (
    <AutenticacionProveedor>
      <Router>
        <Routes>
          {/* Redirigir automáticamente a /login */}
          <Route path="/" element={<Navigate to="/login" />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </Router>
    </AutenticacionProveedor>
  );
};

export default App;
