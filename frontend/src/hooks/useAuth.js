import { useState, useEffect } from 'react';
import api from '../utils/api';
const useAuth = () => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);
  const login = async (username, password) => {
    try {
      const response = await api.post('/auth/login', { username, password });
      setToken(response.data.token);
      setUser(response.data.user);
    } catch (error) {
      console.error(error);
    }
  };
  const register = async (username, email, password) => {
    try {
      const response = await api.post('/auth/register', { username, email, password });
      setToken(response.data.token);
      setUser(response.data.user);
    } catch (error) {
      console.error(error);
    }
  };
  return { user, token, login, register };
};
export default useAuth;