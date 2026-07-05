from fastapi import APIRouter
from embeddings_all_02.embeddings_call import do_doclist_embeddings_call_google, do_doclist_embeddings_call_huggingface, do_doclist_embeddings_call_openai, do_doclist_embeddings_similaritysearch_google, do_doclist_embeddings_similaritysearch_huggingface, do_doclist_embeddings_similaritysearch_openai, do_simple_embeddings_call_google, do_simple_embeddings_call_huggingface, do_simple_embeddings_call_openai
from embeddings_all_02.model.embed_data_model import DocList, DocSearchModel
from models_all_01.model.prompt_query import SimpleQuery

router = APIRouter()

@router.post("/api/embeddings/openai/simplequery")
def simple_embeddings_call_openai(simpleQuery: SimpleQuery):
    return do_simple_embeddings_call_openai(simpleQuery)

@router.post("/api/embeddings/google/simplequery")
def  simple_embeddings_call_openai (simpleQuery: SimpleQuery):
    return do_simple_embeddings_call_google(simpleQuery)

@router.post("/api/embeddings/huggingface/simplequery")
def  simple_embeddings_call_huggingface (simpleQuery: SimpleQuery):
    return do_simple_embeddings_call_huggingface(simpleQuery)


@router.post("/api/embeddings/openai/docslist")
def  doclist_embeddings_call_openai (documents_list: DocList):
    return do_doclist_embeddings_call_openai(documents_list)

@router.post("/api/embeddings/google/docslist")
def  doclist_embeddings_call_openai (documents_list: DocList):
    return do_doclist_embeddings_call_google(documents_list)

@router.post("/api/embeddings/huggingface/docslist")
def  doclist_embeddings_call_huggingface (documents_list: DocList):
    return do_doclist_embeddings_call_huggingface(documents_list)

@router.post("/api/embeddings/openai/similaritysearch")
async def doclist_embeddings_similaritysearch_openai (docSearchModel : DocSearchModel ):
    print("Inside the API Call")
    return await do_doclist_embeddings_similaritysearch_openai(docSearchModel)


@router.post("/api/embeddings/google/similaritysearch")
async def doclist_embeddings_similaritysearch_google (docSearchModel : DocSearchModel ):
    print("Inside the API Call")
    return await do_doclist_embeddings_similaritysearch_google(docSearchModel)

@router.post("/api/embeddings/huggingface/similaritysearch")
async def doclist_embeddings_similaritysearch_huggingface (docSearchModel : DocSearchModel ):
    print("Inside the API Call")
    return await do_doclist_embeddings_similaritysearch_huggingface(docSearchModel)