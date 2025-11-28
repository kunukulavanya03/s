import { useState, useEffect } from 'react';
import api from '../utils/api';
const usePosts = () => {
  const [posts, setPosts] = useState([]);
  const fetchPosts = async () => {
    try {
      const response = await api.get('/posts');
      setPosts(response.data);
    } catch (error) {
      console.error(error);
    }
  };
  useEffect(() => {
    fetchPosts();
  }, []);
  return { posts };
};
export default usePosts;