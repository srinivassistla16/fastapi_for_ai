from pydantic import BaseModel

class DocListForVectorStore(BaseModel):
    docs: list[str]
    metadatas: list[str]


class SimpleQuery(BaseModel):
    query_str: str