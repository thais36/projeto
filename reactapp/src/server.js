const express = require('express');
const path = require('path');

const app = express();
const port = process.env.PORT || 5000;

// Servir arquivos estáticos da pasta 'build'
app.use(express.static(path.join(__dirname, 'build')));

// Rotas do servidor
// ...

// Rota para servir o arquivo HTML do aplicativo React
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

// Iniciar o servidor
app.listen(port, () => {
  console.log(`Servidor iniciado na porta ${port}`);
});
