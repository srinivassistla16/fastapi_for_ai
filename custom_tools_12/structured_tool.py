
from langchain_community.tools import StructuredTool

from custom_tools_12.model.custom_tool_model import CustomToolModel, MultiplyInput


def multiply_func(num1:int, num2:int)->int:
    """Multiply two numbers"""
    return num1 * num2

multiply = StructuredTool.from_function(func=multiply_func, name="multiply tool", description="Multiply two Numbers", args_schema=MultiplyInput)

async def do_multiply_with_structured_tool(customToolModel: CustomToolModel):
    print("StructuredTool")
    product = multiply.invoke({"num1" : customToolModel.num1, "num2": customToolModel.num2 })
    return {"model_response": product, "toolname" : multiply.name, "tooldesc": multiply.description, "toolargs": str(multiply.args_schema.model_json_schema()) }


