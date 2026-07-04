from fastapi import APIRouter, HTTPException
from models_all_01.chat_openai import do_simple_invoke_gemini, do_simple_invoke_huggingface, do_simple_invoke_openai
from models_all_01.model.prompt_query import SimpleQuery


router = APIRouter()



@router.post("/api/models/openai/simplequery")
def get_openai_response(simpleQuery: SimpleQuery):
    return do_simple_invoke_openai(simpleQuery)

@router.post("/api/models/gemini/simplequery")
def get_gemini_response(simpleQuery: SimpleQuery):
    return do_simple_invoke_gemini(simpleQuery)

@router.post("/api/models/huggingface/simplequery")
def get_huggingface_response(simpleQuery: SimpleQuery):
    return do_simple_invoke_huggingface(simpleQuery)
