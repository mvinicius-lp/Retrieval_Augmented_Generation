from langchain_community.embeddings.ollama import OllamaEmbeddings


#Cria uma instância de embeddings (representações vetoriais) baseada no modelo nomic-embed-text
#funcao de incorporacao, para ser usada em dois lugares: 1 - criar o BD e 2 - Consultar o BD.
#representações numéricas de palavras
def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
