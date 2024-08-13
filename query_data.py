import argparse
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

# define um template de prompt, que é uma string de várias linhas usada para estruturar entradas de perguntas
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
restrictions:
- generate the answer in Concrete Experience-Experimental (CE) proposity by Kolb (1984)
"""


def main():
    # cria um CLI básico para processar um texto de consulta fornecido como argumento da linha de comando.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def query_rag(query_text: str):
    # prepara o banco de dados utilizando uma função de incorporação para lidar com consultas de texto.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Pesquisa no banco de dados.
    results = db.similarity_search_with_score(query_text, k=5)

    # formata o texto de contexto usando resultados de uma consulta e gera um prompt estruturado
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # interagir com o modelo de linguagem específico
    model = Ollama(model="mistral")
    response_text = model.invoke(prompt)

    #extrair informações dos resultados de uma consulta (como IDs de documentos), 
    #formata uma resposta composta pela resposta do modelo e os IDs dos documentos
    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text


if __name__ == "__main__":
    main()
