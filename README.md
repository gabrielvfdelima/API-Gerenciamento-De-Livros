# 📚 API de Gerenciamento de Livros

Este é um **projeto básico de API RESTful** desenvolvido em **Python** utilizando o framework *Flask*. A API possibilita a realização de operações CRUD (*Create, Read, Update, Delete*) para gerenciar um pequeno catálogo de livros.

Este projeto foi criado como um exercício de aprendizado, com foco no uso de boas práticas de manipulação de dados em Python e no desenvolvimento de APIs para aplicações mais escaláveis.


## 🚀 Funcionalidades

A API permite as seguintes operações:

1. **Listar todos os livros**  
   **Endpoint:** `GET /livros`  
   Retorna todos os livros atualmente cadastrados no sistema.

2. **Consultar um livro específico pelo ID**  
   **Endpoint:** `GET /livros/<id>`  
   Substitua `<id>` pelo ID do livro.  
   Retorna as informações do livro correspondente, caso o ID exista no catálogo.

3. **Adicionar um novo livro**  
   **Endpoint:** `POST /livros`  
   Envie os dados do novo livro no corpo da requisição em formato JSON.  
   Um novo livro será cadastrado e adicionado à lista.

4. **Editar as informações de um livro existente**  
   **Endpoint:** `PUT /livros/<id>`  
   Substitua `<id>` pelo ID do livro e envie no corpo da requisição os dados atualizados em formato JSON.  
   O livro correspondente será atualizado.

5. **Excluir um livro pelo ID**  
   **Endpoint:** `DELETE /livros/<id>`  
   Substitua `<id>` pelo ID do livro a ser excluído.  
   Remove o livro do catálogo.


## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Flask**  
  Framework leve para desenvolvimento de APIs em Python.


## 📂 Estrutura de Dados

Os dados dos livros estão organizados como um dicionário aninhado. Cada livro é representado por um ID (chave), e os detalhes do livro são armazenados em forma de outro dicionário com as seguintes propriedades:
- `titulo`: Título do livro.
- `autor`: Nome do autor.

Exemplo de estrutura utilizada:

    1: {'titulo': 'O Senhor dos Anéis - A Sociedade do Anel', 'autor': 'J.R.R Tolkien'},
    2: {'titulo': 'Cristianismo Puro e Simples', 'autor': 'C.S. Lewis'},
    3: {'titulo': 'A Esperança do Evangelho', 'autor': 'Chesterton'},


🔗 Próximos Passos

Este projeto poderia ser expandido para incluir as seguintes melhorias:

Adicionar persistência de dados, utilizando um banco de dados como SQLite ou PostgreSQL.
Melhorar o tratamento de erros para lidar com requisições inválidas ou IDs não existentes.
Implementar autenticação para proteger os endpoints da API.
Adicionar testes automatizados para garantir a confiabilidade.

Este é apenas o início da jornada para aprender sobre desenvolvimento back-end e APIs RESTful! 🚀

👤 Autor:
Gabriel Veloso

Fique à vontade para entrar em contato ou deixar sugestões! 😊