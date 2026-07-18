from fastapi import APIRouter

from retriever_all_11.model.retriever_model import SimpleQuery
from retriever_all_11.retriever_call import do_rerieve_from_wikipedia

router = APIRouter()

@router.post("/api/retriever/wikipediaretriever")
async def rerieve_from_wikipedia(simpleQuery: SimpleQuery):
    return await do_rerieve_from_wikipedia(simpleQuery)