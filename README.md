Projeto de Indexação e Consulta de Documentos com LangChain

Este projeto visa fornecer uma solução completa para indexar documentos PDF e realizar consultas baseadas em Retrieval-Augmented Generation (RAG) utilizando a biblioteca LangChain. Ele é composto por dois scripts principais:

1. `populate_database.py`: Responsável por carregar, dividir e adicionar documentos PDF ao banco de dados vetorial.
2. `get-embedding_function.py.py`: Funcão de incorporação para geração dos embeddings.
3. `query_rag.py`: Permite realizar consultas sobre o banco de dados utilizando um modelo de linguagem para gerar respostas baseadas no contexto dos documentos.


Estrutura do Projeto


/project-root
│
├── data/                   # Diretório contendo os arquivos PDF para processamento
├── chroma/                 # Diretório onde o banco de dados vetorial é armazenado
├── populate_database.py      # Script para indexar documentos PDF
├── query_rag.py            # Script para consultar o banco de dados vetorial
├── get_embedding_function.py # Função para obter a função de incorporação de embeddings
└── README.md               # Este arquivo


Dependências

Certifique-se de ter as seguintes bibliotecas instaladas:

- `argparse`
- `os`
- `shutil`
- `langchain_community`
- `langchain_text_splitters`
- `langchain.schema`
- `get_embedding_function`
- `langchain.prompts`
- `langchain.llms`

Você pode instalar as dependências necessárias utilizando o `pip`:

```
pip install langchain_community langchain_text_splitters langchain
```

Uso

Indexação de Documentos

Para indexar documentos PDF e adicionar ao banco de dados vetorial, execute o seguinte comando:

```
python index_documents.py [--reset]
```

- `--reset`: Opcional. Use esta flag para limpar o banco de dados vetorial antes de adicionar novos documentos.

Este script realiza as seguintes etapas:
1. Carregamento de Documentos: Carrega documentos PDF do diretório `data/`.
2. Divisão de Documentos: Divide os documentos em chunks menores para melhor processamento.
3. Adição ao Banco de Dados: Adiciona chunks ao banco de dados vetorial (`chroma/`).

Consulta ao Banco de Dados

Para consultar o banco de dados e obter respostas baseadas em um texto de consulta, execute o seguinte comando:

```
python query_rag.py "Texto da consulta"
```

Este script realiza as seguintes etapas:
1. Pesquisa no Banco de Dados: Realiza uma pesquisa no banco de dados vetorial usando o texto de consulta.
2. Geração de Resposta: Usa um modelo de linguagem para gerar uma resposta baseada no contexto dos documentos recuperados.

Scripts

`populate_database.py`

Este script é responsável por indexar documentos PDF no banco de dados vetorial.

- Funções principais:
  - `load_documents()`: Carrega documentos PDF do diretório `data/`.
  - `split_documents(documents)`: Divide documentos em partes menores.
  - `add_to_chroma(chunks)`: Adiciona documentos ao banco de dados vetorial `chroma/`.
  - `calculate_chunk_ids(chunks)`: Calcula IDs únicos para cada chunk de documento.
  - `clear_database()`: Limpa o banco de dados vetorial.

`query_rag.py`

Este script permite realizar consultas e obter respostas com base no banco de dados vetorial.

- Funções principais:
  - `query_rag(query_text)`: Realiza uma consulta no banco de dados e gera uma resposta com base no contexto dos documentos recuperados.

Função de Incorporação

A função `get_embedding_function()` retorna uma função de incorporação baseada no modelo `nomic-embed-text`, usada para gerar representações vetoriais dos documentos.

Contribuição

Se você quiser contribuir para este projeto, sinta-se à vontade para enviar pull requests ou relatar problemas.
