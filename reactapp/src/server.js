const express = require('express');
const path = require('path');

const app = express();
const port = process.env.PORT || 5000;

// Servir os arquivos estáticos do React
app.use(express.static(path.join(__dirname, 'build')));

// Rota para servir o arquivo HTML do React
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

// Resto do código do servidor...

// Iniciar o servidor
app.listen(port, () => {
  console.log(`Servidor iniciado na porta ${port}`);
});

Path: reactapp\src\index.js
/* eslint-disable no-lone-blocks */
/* eslint-disable no-unused-vars */
import React from 'react';
