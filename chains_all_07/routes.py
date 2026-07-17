from fastapi import APIRouter

from chains_all_07.chains_call import do_parallel_chain_summary, do_sequential_chain_summary
from output_parsers_all_06.model.output_parser_model import ParserModel
from output_parsers_all_06.output_parser_call import do_pydantic_output_parser_sentiment
router = APIRouter()

@router.post("/api/chains/sequential/summary")
async def sequential_chain_summary(parserModel: ParserModel):
    return await do_sequential_chain_summary(parserModel)

@router.post("/api/chains/parallel/summary")
async def parallel_chain_summary(parserModel: ParserModel):
    return await do_parallel_chain_summary(parserModel)

@router.post("/api/chains/parallel/summary")
async def parallel_chain_summary(parserModel: ParserModel):
    return await do_parallel_chain_summary(parserModel)

@router.post("/api/chains/conditional/summary")
async def pydantic_output_parser_sentiment(parserModel: ParserModel):
    return await do_pydantic_output_parser_sentiment(parserModel)

