from unittest import result

from fastapi import HTTPException
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
#from torch import cosine_similarity
from embeddings_all_02.model.embed_data_model import DocList, DocSearchModel
from models_all_01.model.prompt_query import SimpleQuery

import torch
from torch.nn.functional import cosine_similarity



def do_simple_embeddings_call_openai(simpleQuery: SimpleQuery):
    try:
        query_str = simpleQuery.query_str
        embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)
        result = embedding.embed_query(query_str)
        return {"model_response": str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def do_simple_embeddings_call_google(simpleQuery: SimpleQuery):
    try:
        query_str = simpleQuery.query_str
        embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",dimensions=32)
        result = embedding.embed_query(query_str)
        return {"model_response" : str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def do_simple_embeddings_call_huggingface(simpleQuery: SimpleQuery):
    try:
        query_str = simpleQuery.query_str
        embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        result = embedding.embed_query(query_str)
        return {"model_response" : str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def do_doclist_embeddings_call_openai(docList: DocList):
    try:
        docs = docList.docs
        embedding = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)
        result = embedding.embed_documents(docs)
        return {"model_response" : str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def do_doclist_embeddings_call_google(docList: DocList):
    try:
        docs = docList.docs
        embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",dimensions=32)
        result = embedding.embed_documents(docs)
        return {"model_response" : str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def do_doclist_embeddings_call_huggingface(docList: DocList):
    try:
        docs = docList.docs
        embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        result = embedding.embed_documents(docs)
        return {"model_response" : str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def do_doclist_embeddings_similaritysearch_openai(docSearchModel: DocSearchModel):
    try:
        docs = docSearchModel.docsList
        query_str = docSearchModel.query
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)
        docs_embeddings = torch.tensor(
        embedding_model.embed_documents(docs),
        dtype=torch.float32
        )
        query_embedding = torch.tensor(
        embedding_model.embed_query(query_str),
        dtype=torch.float32
        )
        result_tensor = cosine_similarity(docs_embeddings, query_embedding, dim=1)
        result = result_tensor.tolist()
        index, score = sorted(list(enumerate(result)), key=lambda x: x[1], reverse=True)[0]
        print(f"Most similar document index: {index}, Score: {score}")
        return {"model_response" : str(result), "similar_sentence": docs[index]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def do_doclist_embeddings_similaritysearch_google(docSearchModel: DocSearchModel):
    try:
        docs = docSearchModel.docsList
        query_str = docSearchModel.query
        embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",dimensions=32)
        docs_embeddings = torch.tensor(
        embedding_model.embed_documents(docs),
        dtype=torch.float32
        )
        query_embedding = torch.tensor(
        embedding_model.embed_query(query_str),
        dtype=torch.float32
        )
        result_tensor = cosine_similarity(docs_embeddings, query_embedding, dim=1)
        result = result_tensor.tolist()
        index, score = sorted(list(enumerate(result)), key=lambda x: x[1], reverse=True)[0]
        print(f"Most similar document index: {index}, Score: {score}")
        return {"model_response" : str(result), "similar_sentence": docs[index]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def do_doclist_embeddings_similaritysearch_huggingface(docSearchModel: DocSearchModel):
    try:
        docs = docSearchModel.docsList
        query_str = docSearchModel.query
        embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        docs_embeddings = torch.tensor(
        embedding_model.embed_documents(docs),
        dtype=torch.float32
        )
        query_embedding = torch.tensor(
        embedding_model.embed_query(query_str),
        dtype=torch.float32
        )
        result_tensor = cosine_similarity(docs_embeddings, query_embedding, dim=1)
        result = result_tensor.tolist()
        index, score = sorted(list(enumerate(result)), key=lambda x: x[1], reverse=True)[0]
        print(f"Most similar document index: {index}, Score: {score}")
        return {"model_response" : str(result), "similar_sentence": docs[index]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
