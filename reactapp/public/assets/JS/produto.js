document.getElementById('productForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o comportamento padrão do formulário
  
    // Obtém os valores dos campos do formulário
    const image = document.getElementById('image').files[0];
    const name = document.getElementById('name').value;
    const price = document.getElementById('price').value;
    const color = document.getElementById('color').value;
    const size = document.getElementById('size').value;
  
    // Cria um novo elemento de lista para exibir o produto
    const listItem = document.createElement('li');
  
    // Cria uma imagem e atribui a imagem selecionada ao atributo src
    const imgElement = document.createElement('img');
    imgElement.src = URL.createObjectURL(image);
    listItem.appendChild(imgElement);
  
    // Cria um elemento de parágrafo para exibir os detalhes do produto
    const detailsElement = document.createElement('p');
    detailsElement.textContent = `Nome: ${name}, Preço: R$ ${price}, Cor: ${color}, Tamanho: ${size}`;
    listItem.appendChild(detailsElement);
  
    // Adiciona o novo item de lista à lista de produtos
    document.getElementById('productList').appendChild(listItem);
  
    // Limpa os campos do formulário após a submissão
    document.getElementById('image').value = '';
    document.getElementById('name').value = '';
    document.getElementById('price').value = '';
    document.getElementById('color').value = '';
    document.getElementById('size').value = '';
  });
  