from custom_tools_12.model.custom_tool_model import CustomToolModel, MultiplyTool


async def do_multiply_with_base_tool(customToolModel: CustomToolModel):
    print("BASE TOOL")
    multiply = MultiplyTool()
    product = multiply.invoke({"num1" : customToolModel.num1, "num2": customToolModel.num2 })
    return {"model_response": product, "toolname" : multiply.name, "tooldesc": multiply.description, "toolargs": str(multiply.args_schema.model_json_schema()) }
