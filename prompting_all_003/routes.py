from fastapi import APIRouter

from prompting_all_003.model.prompt_data_model import PromptDataModel
from prompting_all_003.prompt_call import do_promptcall_using_datamodel_gemini, do_promptcall_using_datamodel_huggingface, do_promptcall_using_datamodel_openai

router = APIRouter()

@router.post("/api/prompting/openai/promptcall")
async def promptcall_using_datamodel_openai (promptDataModel : PromptDataModel ):
    return await do_promptcall_using_datamodel_openai(promptDataModel)

@router.post("/api/prompting/google/promptcall")
async def promptcall_using_datamodel_gemini (promptDataModel : PromptDataModel ):
    return await do_promptcall_using_datamodel_gemini(promptDataModel)

@router.post("/api/prompting/huggingface/promptcall")
async def promptcall_using_datamodel_huggingface (promptDataModel : PromptDataModel ):
    return await do_promptcall_using_datamodel_huggingface(promptDataModel)
