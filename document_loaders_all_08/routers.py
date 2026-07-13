from fastapi import APIRouter
from langchain_community.document_loaders import TextLoader

from document_loaders_all_08.document_loader_calls import do_document_load_pdf_file, do_document_load_text_file
from document_loaders_all_08.model.document_loader_model import DocumentFile


router = APIRouter()

@router.post("/api/documentloader/textloader")
async def document_load_text_file(docFile: DocumentFile):
    return await do_document_load_text_file(docFile)

@router.post("/api/documentloader/pdfloader")
async def document_load_text_file(docFile: DocumentFile):
    return await do_document_load_pdf_file(docFile)
