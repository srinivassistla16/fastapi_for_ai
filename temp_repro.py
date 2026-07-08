import asyncio
from output_parsers_all_06.output_parser_call import do_str_output_parser_detail
from output_parsers_all_06.model.output_parser_model import ParserModel

async def main():
    try:
        result = await do_str_output_parser_detail(ParserModel(topic='AI'))
        print(result)
    except Exception as e:
        import traceback
        traceback.print_exc()

asyncio.run(main())
