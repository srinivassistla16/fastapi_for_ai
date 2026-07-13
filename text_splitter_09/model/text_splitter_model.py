from pydantic import BaseModel

class DocumentWrapper(BaseModel):
    document_file_name: str