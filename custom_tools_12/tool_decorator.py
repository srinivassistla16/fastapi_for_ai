from langchain_community.tools import tool

from custom_tools_12.model.custom_tool_model import CustomToolModel

@tool
def multiply(num1: int, num2: int) -> int:
    """"Multiply Two Numbers"""
    return num1 * num2



async def do_multiply_with_tool_decorator(customToolModel: CustomToolModel):
    product = multiply.invoke({"num1" : customToolModel.num1, "num2": customToolModel.num2 })
    return {"model_response": product, "toolname" : multiply.name, "tooldesc": multiply.description, "toolargs": str(multiply.args_schema.model_json_schema()) }