import { Link } from 'react-router-dom';
import "./narvar.css";

function Navbar() {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/perfil">perfil</Link>
  
    </nav>
  );
}

export default Navbar;
