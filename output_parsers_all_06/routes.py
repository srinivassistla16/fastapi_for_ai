from fastapi import APIRouter

from output_parsers_all_06.model.output_parser_model import ParserModel
from output_parsers_all_06.output_parser_call import do_str_output_parser_detail, do_str_output_parser_summary

router = APIRouter()


@router.post("/api/outputparsers/stroutputparser/detail")
async def str_output_parser_detail(parserModel: ParserModel):
    return await do_str_output_parser_detail(parserModel)

@router.post("/api/outputparsers/stroutputparser/summary")
async def str_output_parser_summary(parserModel: ParserModel):
    return await do_str_output_parser_summary(parserModel)