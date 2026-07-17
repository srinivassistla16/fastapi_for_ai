from fastapi import HTTPException
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from vector_store_all_10.model.chroma_model import DocListForVectorStore, SimpleQuery

#persist_directory = 'VECTOR_STORE_DB/chroma_db'
persist_directory = 'VECTOR_STORE_DB/repeating_data_chroma_db'

async def do_store_vectors_openai(docListForVectorStore: DocListForVectorStore):
    # step 1: Add all documents to a list
    docs : list[Document] = []
    for i in range(4):
        doc = Document(
            page_content= docListForVectorStore.docs[i],
            metadata = { "subject" : docListForVectorStore.metadatas[i]}
        )
        docs.append(doc)
    # step 2: Define the persistent vector store
    vector_store = Chroma(
        embedding_function = OpenAIEmbeddings(),
        persist_directory = persist_directory,
        collection_name = "cities"
    )
    list_of_embedding_vector = vector_store.add_documents(docs)
    
    dict_full_data = vector_store.get(include = ['embeddings','documents','metadatas'])
    return {"model_response" : str(dict_full_data)}

async def do_similarity_search_in_vectorstore_openai(simpleQuery: SimpleQuery):
    vector_store = Chroma(
        embedding_function = OpenAIEmbeddings(),
        persist_directory = persist_directory,
        collection_name = "cities"
    )
    res1 = vector_store.similarity_search(simpleQuery.query_str, k = 1)
    res2 = vector_store.similarity_search_with_score(simpleQuery.query_str, k = 1)
    return {"model_response" : str(res1[0].page_content), "similarity_with_score":  str(res2)}