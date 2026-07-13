from pydantic import BaseModel


class DocumentFile(BaseModel):
    document_file_name: str
    page_no: int = 0


