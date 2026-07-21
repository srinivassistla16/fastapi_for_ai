
from typing import Type

from langchain_community.tools import BaseTool
from pydantic import BaseModel, Field



class CustomToolModel(BaseModel):
    num1: int
    num2: int


class MultiplyInput(BaseModel):
    num1 : int = Field(description="Number 1 for multiplication", required=True)
    num2 : int = Field(description="Number 2 for multiplication", required=True)

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description:str = "Multiply Two Numbers"
    args_schema : Type[BaseModel] = MultiplyInput
    
    def _run(self, num1:int, num2:int)->int:
        return num1 * num2