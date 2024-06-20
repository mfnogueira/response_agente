from langchain.vectorstores import VectorStore

# Configurando os caminhos para as bases de vetores
VECTOR_STORE_PATHS = {
    "futebol": "data/futebol/vectorstore",
    "volei": "data/volei/vectorstore",
    "basquete": "data/basquete/vectorstore",
    "ufc": "data/ufc/vectorstore",
    "formula1": "data/formula1/vectorstore"
}

# Inicializando as bases de vetores
vector_stores = {
    specialty: VectorStore(path)
    for specialty, path in VECTOR_STORE_PATHS.items()
}
