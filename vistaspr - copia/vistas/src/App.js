import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/narvar';
import Home from './pages/home';
import About from './pages/about';
import Servicios from './pages/servicios';
import Perfil from './components/perfil';
import Registrarse from './pages/registrarse';
import PerfilContratista from "./pages/perfilcontratista";
import FormularioLogin from './pages/formulario_login';
import './App.css';


function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/services" element={<Servicios />} />
        <Route path="/profile" element={<Perfil />} />
        <Route path="/registrarse" element={<Registrarse />} />
        <Route path="/perfil/:id" element={<PerfilContratista />} />
        <Route path="/formulario_login" element={<FormularioLogin />} />
        <Route path="/perfilcontratista" element={<PerfilContratista />} />
      </Routes>
    </Router>
  );
}

export default App;
