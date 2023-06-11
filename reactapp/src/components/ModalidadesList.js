import React, { useEffect, useState } from 'react';
import { getModalidades } from './api';

const ModalidadesList = () => {
  const [modalidades, setModalidades] = useState([]);

  useEffect(() => {
    fetchModalidades();
  }, []);

  const fetchModalidades = async () => {
    try {
      const data = await getModalidades();
      setModalidades(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Lista de Modalidades</h1>
      <ul>
        {modalidades.map(modalidade => (
          <li key={modalidade.id}>{modalidade.nome}</li>
        ))}
      </ul>
    </div>
  );
};

export default ModalidadesList;
