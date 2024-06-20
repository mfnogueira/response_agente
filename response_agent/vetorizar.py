import os
import pandas as pd
from PyPDF2 import PdfFileReader
from langchain.vectorstores import VectorStore

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def vetorizar_csv(file_path, vector_store_path):
    df = pd.read_csv(file_path)
    texts = df.to_string(index=False).split('\n')
    vetorizar_e_salvar(texts, vector_store_path)

def vetorizar_pdf(file_path, vector_store_path):
    with open(file_path, 'rb') as f:
        reader = PdfFileReader(f)
        texts = []
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            texts.append(page.extract_text())
        vetorizar_e_salvar(texts, vector_store_path)

def vetorizar_e_salvar(texts, vector_store_path):
    vector_store = VectorStore()
    for text in texts:
        vector_store.add_text(text)
    ensure_directory_exists(vector_store_path)
    vector_store.save(vector_store_path)

def vetorizar(file_path, specialty):
    ext = os.path.splitext(file_path)[-1].lower()
    vector_store_path = f"data/{specialty}/vectorstore"
    ensure_directory_exists(os.path.dirname(vector_store_path))
    if ext == ".csv":
        vetorizar_csv(file_path, vector_store_path)
    elif ext == ".pdf":
        vetorizar_pdf(file_path, vector_store_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

if __name__ == "__main__":
    # Exemplo de uso:
    vetorizar("path/to/your/file.csv", "futebol")
    vetorizar("path/to/your/file.pdf", "formula1")




# from response_agent.vetorizar import vetorizar

# # Vetorizar um arquivo CSV para a especialidade "futebol"
# vetorizar("path/to/your/file.csv", "futebol")

# # Vetorizar um arquivo PDF para a especialidade "formula1"
# vetorizar("path/to/your/file.pdf", "formula1")
