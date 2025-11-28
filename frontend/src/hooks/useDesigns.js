import { useState, useEffect } from 'react';
import api from '../utils/api';
const useDesigns = () => {
  const [designs, setDesigns] = useState([]);
  const fetchDesigns = async () => {
    try {
      const response = await api.get('/designs');
      setDesigns(response.data);
    } catch (error) {
      console.error(error);
    }
  };
  useEffect(() => {
    fetchDesigns();
  }, []);
  return { designs };
};
export default useDesigns;