from pydantic import BaseModel

class SimpleQuery(BaseModel):
    query_str: str