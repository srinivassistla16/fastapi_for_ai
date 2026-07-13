from fastapi import APIRouter

from output_parsers_all_06.model.output_parser_model import ParserModel
from output_parsers_all_06.output_parser_call import do_json_output_parser_summary, do_pydantic_output_parser_sentiment, do_str_output_parser_detail, do_str_output_parser_summary

router = APIRouter()


@router.post("/api/outputparsers/stroutputparser/detail")
async def str_output_parser_detail(parserModel: ParserModel):
    return await do_str_output_parser_detail(parserModel)

@router.post("/api/outputparsers/stroutputparser/summary")
async def str_output_parser_summary(parserModel: ParserModel):
    return await do_str_output_parser_summary(parserModel)


@router.post("/api/outputparsers/jsonoutputparser/detail")
async def json_output_parser_summary(parserModel: ParserModel):
    return await do_json_output_parser_summary(parserModel)

@router.post("/api/outputparsers/pydanticoutputparser/sentiment")
async def pydantic_output_parser_sentiment(parserModel: ParserModel):
    return await do_pydantic_output_parser_sentiment(parserModel)


