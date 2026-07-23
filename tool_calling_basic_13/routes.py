from fastapi import APIRouter

from tool_calling_basic_13.basic_multiply_tool_calling import do_tool_calling_for_multiplier
from tool_calling_basic_13.model.tool_call_model import SimpleQuery

router = APIRouter()

@router.post("/api/toolcallingbasic/multiplier")
async def tool_calling_for_multiplier(simpleQuery: SimpleQuery):
    return await do_tool_calling_for_multiplier(simpleQuery)