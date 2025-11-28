import React from 'react';
import { Link } from 'react-router-dom';
function Header() {
  return (
    <header className="bg-blue-500 text-white py-4">
      <nav className="container mx-auto flex justify-between">
        <Link to="/" className="text-3xl font-bold">Logo</Link>
        <ul className="flex items-center space-x-4">
          <li><Link to="/about" className="text-lg">About</Link></li>
          <li><Link to="/blog" className="text-lg">Blog</Link></li>
          <li><Link to="/contact" className="text-lg">Contact</Link></li>
        </ul>
      </nav>
    </header>
  );
}
export default Header;