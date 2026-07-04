from pydantic import BaseModel
from typing import List

class DocList(BaseModel):
    docs: list[str]


class DocSearchModel(BaseModel):
    docsList: list[str]
    query: str
    