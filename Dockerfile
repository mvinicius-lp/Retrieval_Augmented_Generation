# Use a imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copie todo o código fonte para o diretório de trabalho no contêiner
COPY . .

# Comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "populate_database.py"]
