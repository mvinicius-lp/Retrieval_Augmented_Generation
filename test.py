#importa e exibe as versões das bibliotecas langchain e chromadb
from langchain import __version__ as langchain_version
from chromadb import __version__ as chromadb_version

print(f"Langchain version: {langchain_version}")
print(f"Chromadb version: {chromadb_version}")
