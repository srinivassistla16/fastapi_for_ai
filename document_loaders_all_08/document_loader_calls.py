

from langchain_community.document_loaders import PyPDFLoader, TextLoader

from document_loaders_all_08.model.document_loader_model import DocumentFile

DEST_DOCS_FOLDER = "DEST_DOCS_FOR_AI"

async def do_document_load_text_file(docFile: DocumentFile):
    try:
        loader = TextLoader(DEST_DOCS_FOLDER+"\\"+ docFile.document_file_name, encoding="utf-8")
        docs = loader.load()
        return {"model_response": docs[0].page_content, "no_of_docs" : len(docs)}
    except Exception as e:
        return {"model_response": "Exception Occured!!"}
    
async def do_document_load_pdf_file(docFile: DocumentFile):
    loader = PyPDFLoader(DEST_DOCS_FOLDER+"\\"+ docFile.document_file_name)
    #loader = TextLoader(DEST_DOCS_FOLDER+"\\"+ docFile.document_file_name, encoding="utf-8")
    docs = loader.load()
    return {"model_response": docs[docFile.page_no - 1].page_content, "no_of_docs" : len(docs)}
   