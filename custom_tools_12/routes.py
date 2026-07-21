
from fastapi import APIRouter

from custom_tools_12.model.custom_tool_model import CustomToolModel

from custom_tools_12.base_tool import do_multiply_with_base_tool
from custom_tools_12.structured_tool import do_multiply_with_structured_tool
from custom_tools_12.tool_decorator import do_multiply_with_tool_decorator


router = APIRouter()

@router.post("/api/customtool/tooldecorator/call")
async def multiply_with_tool_decorator(customToolModel: CustomToolModel):
    return await do_multiply_with_tool_decorator(customToolModel)

@router.post("/api/customtool/structuredtool/call")
async def multiply_with_structured_tool(customToolModel: CustomToolModel):
    return await do_multiply_with_structured_tool(customToolModel)

@router.post("/api/customtool/basetool/call")
async def multiply_with_base_tool(customToolModel: CustomToolModel):
    return await do_multiply_with_base_tool(customToolModel)