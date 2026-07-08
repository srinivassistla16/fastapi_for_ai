from fastapi import HTTPException

from langchain_google_genai import ChatGoogleGenerativeAI

from structured_output_all_05.model.review_model import Review, ReviewPydanticModel, UserComment, json_schema


async def do_structured_output_typeddict_call(userComment: UserComment):
    
    model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.9)
    structured_model = model.with_structured_output(Review)
    structured_model_response = structured_model.invoke(userComment.user_comment_str)
    return {"model_response" : str(structured_model_response)}
   
async def do_structured_output_pydantic_call(userComment: UserComment):
    model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.9)
    structured_model = model.with_structured_output(ReviewPydanticModel)
    structured_model_response = structured_model.invoke(userComment.user_comment_str)
    return {"model_response" : str(structured_model_response)}

async def do_structured_output_jsonschema_call(userComment: UserComment):
    model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.9)
    structured_model = model.with_structured_output(json_schema)
    structured_model_response = structured_model.invoke(userComment.user_comment_str)
    return {"model_response" : str(structured_model_response)}
   