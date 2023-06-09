import React, { useState, useEffect } from "react";
import axios from "axios";
import ListaProdutos from "./lista_produtos";
import produto from "./produto";

function ListaProdutos() {
  const [produtos, setProdutos] = useState([]);

  useEffect(() => {
    axios.get("/api/produtos").then((response) => {
      setProdutos(response.data);
    });
  }, []);

  return (
    <div>
      <h1>Lista de produtos</h1>
      <ul>
        {produtos.map((produto) => (
          <li key={produto.id}>
            <img src={produto.imagem} alt={produto.titulo} />
            <h2>{produto.titulo}</h2>
            <p>Tamanho: {produto.tamanho}</p>
            <p>Cor: {produto.cor}</p>
            <p>Preço: R$ {produto.preco.toFixed(2)}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ListaProdutos;