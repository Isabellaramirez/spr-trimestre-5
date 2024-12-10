import React from 'react';
import { Link } from 'react-router-dom'; // Para usar Link en lugar de href
import './home.css';

function Home() {
  return (
    <div className="home-container">
      {/* Barra de navegación */}
      <header className="navbar">
        <div className="logo">SPR</div>
        <nav className="nav-links">
          {/* Usamos Link de React Router para navegar */}
          <Link to="/formulario_login">Iniciar Sesión</Link>
          <Link to="/registrarse">Registrarse</Link>
        </nav>
      </header>

      {/* Contenido principal */}
      <main className="main-content">
        <img src="/path/to/logo.png" alt="Logo SPR" className="home-logo" />
        <h1>¿QUIÉNES SOMOS?</h1>
        <p>
          Somos una página confiable, creada por estudiantes del SENA. Esta página
          hará una conexión entre el contratista y el prestador de servicios, con el
          fin de que el prestador suba en lo que se especializa y el contratista
          pueda adquirir sus servicios.
        </p>
      </main>

      {/* Sección de servicios */}
      <section className="services-section">
        <h2>NUESTROS SERVICIOS</h2>
        <p>Conecta con los mejores especialistas en cada área.</p>
      </section>
    </div>
  );
}

export default Home;
