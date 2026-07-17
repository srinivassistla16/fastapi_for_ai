from fastapi import APIRouter

from vector_store_all_10.chroma_store_call import do_similarity_search_in_vectorstore_openai, do_store_vectors_openai
from vector_store_all_10.model.chroma_model import DocListForVectorStore, SimpleQuery

router = APIRouter()

@router.post("/api/vectorstore/openai/store")
async def store_vectors_openai(docListForVectorStore: DocListForVectorStore):
    return  await do_store_vectors_openai(docListForVectorStore)

@router.post("/api/vectorstore/openai/similaritysearch")
async def similarity_search_in_vectorstore_openai(simpleQuery: SimpleQuery):
    return  await do_similarity_search_in_vectorstore_openai(simpleQuery)