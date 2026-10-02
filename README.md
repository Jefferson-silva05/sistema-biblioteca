## Sistema de Biblioteca 

Um sistema de gerenciamento de biblioteca desenvolvido em Python, com o objetivo de praticar lógica de programação, organização de código e manipulação de arquivos JSON.

# Sobre o projeto

O projeto permite gerenciar um pequeno acervo de livros por meio de um menu interativo no terminal. Nele, é possível cadastrar, consultar, listar, atualizar e remover livros, mantendo os dados salvos mesmo após encerrar o programa.

Funcionalidades

- Cadastrar livros com ID, título, autor e ano de publicação.
- Listar todos os livros cadastrados.
- Buscar livros pelo ID ou título.
- Atualizar a disponibilidade dos livros.
- Remover livros do acervo.
- Validar entradas do usuário para evitar dados inválidos.
- Salvar e carregar informações utilizando arquivos JSON.

Tecnologias utilizadas

- Python: Linguagem utilizada no desenvolvimento.
- JSON: Utilizado para armazenar os dados dos livros.
- Bibliotecas nativas: "json" e "time".

Estrutura do projeto

biblioteca/
│
├── biblioteca.py
├── modulobiblioteca.py
├── arquivo_biblioteca.py
├── biblioteca.json
└── README.md

Organização dos arquivos:

- "biblioteca.py": Arquivo principal, responsável pelo menu e funcionamento do sistema.
- "modulobiblioteca.py": Contém funções de validação e tratamento de entradas.
- "arquivo_biblioteca.py": Responsável pelas operações de leitura, gravação, busca e exclusão de livros.
- "biblioteca.json": Arquivo utilizado para armazenar os dados.

Como executar

Pré-requisitos:

- Python 3.10 ou superior.

Passos:

1. Clone o repositório:

git clone URL_DO_REPOSITORIO

2. Acesse a pasta do projeto:

cd biblioteca

3. Execute o arquivo principal:

python biblioteca.py

Observação: O caminho utilizado para salvar o arquivo JSON está definido no código. Caso necessário, ajuste essa localização para corresponder à estrutura das pastas do seu computador.

Objetivo de aprendizagem

Este projeto foi desenvolvido como prática de programação em Python, buscando aprimorar conhecimentos sobre funções, estruturas de repetição, condicionais, listas, dicionários, modularização e manipulação de arquivos.