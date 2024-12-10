import React from "react";
import Home from "./pages/Home";
import './home.css'

function App() {
  return (
    <nav className="nav-links">
    <a href="/login">Iniciar Sesión</a>
    <a href="/register">Registrarse</a>
    <a href="/contractor">Contratista</a>
    <a href="/provider">Prestador Servicios</a>
  </nav>
  
  );
}

export default App;
