import chromadb
from chromadb.utils import embedding_functions

# Instantiate chromadb instance. Data is stored in memory only.
# chroma_client = chromadb.Client()

# Instantiate chromadb instance. Data is stored on disk (a folder named 'my_vectordb' will be created in the same folder as this file).

def vector(sql_statement,tables):
    documents = []

# Store the corresponding menu item IDs in this array.
    metadatas = []

    # Each "document" needs a unique ID.
    ids = []
    id = 1

    # Loop through each SQL statement and populate the arrays.
    for sql in sql_statements:
        documents.append(sql)
        metadatas.append({"item_id": tables[0]})
        ids.append(str(id))
        id += 1
    chroma_client = chromadb.Client()
    chroma_client = chromadb.PersistentClient(path="my_vectordb") 
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")
    collection = chroma_client.get_or_create_collection(name="my_collection", embedding_function=sentence_transformer_ef)
    collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
    )

return collection


def query(collection, word):
    results = collection.query(
    query_texts=[word],
    n_results=5,
    include=['documents', 'distances', 'metadatas']
    )
    print(results['documents'])
    return results['documents']