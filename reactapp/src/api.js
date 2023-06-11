import axios from 'axios';
import { BrowserRouter, Route } from 'react-router-dom';

const API_URL = 'http://localhost:8000/admin/modalidade/modalidade'; // Certifique-se de usar o URL correto do seu backend Django

export const getModalidades = () => {
  return axios.get(`${API_URL}/modalidade/`)
    .then(response => response.data)
    .catch(error => {
      throw error;
    });
};

export const salvarModalidade = (nome) => {
  return axios.post(`${API_URL}/salvar/`, { nome })
    .then(response => response.data)
    .catch(error => {
      throw error;
    });
};

export const editarModalidade = (id) => {
  return axios.get(`${API_URL}/editar/${id}/`)
    .then(response => response.data)
    .catch(error => {
      throw error;
    });
};

export const updateModalidade = (id, nome) => {
  return axios.post(`${API_URL}/update/${id}/`, { nome })
    .then(response => response.data)
    .catch(error => {
      throw error;
    });
};

export const deleteModalidade = (id) => {
  return axios.post(`${API_URL}/delete/${id}/`)
    .then(response => response.data)
    .catch(error => {
      throw error;
    });
};
