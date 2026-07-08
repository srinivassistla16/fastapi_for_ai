
import string
from typing import TypedDict

from fastapi import APIRouter

from structured_output_all_05.model.review_model import UserComment
from structured_output_all_05.structured_analysis import do_structured_output_jsonschema_call, do_structured_output_pydantic_call, do_structured_output_typeddict_call


router = APIRouter()
@router.post("/api/structuredoutput/typeddict/call")
async def structured_output_typeddict_call(userComment: UserComment):
    return await do_structured_output_typeddict_call(userComment)

@router.post("/api/structuredoutput/pydantic/call")
async def structured_output_pydantic_call(userComment: UserComment):
    return await do_structured_output_pydantic_call(userComment)

@router.post("/api/structuredoutput/jsonschema/call")
async def structured_output_jsonschema_call(userComment: UserComment):
    return await do_structured_output_jsonschema_call(userComment)