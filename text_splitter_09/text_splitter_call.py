from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from text_splitter_09.model.text_splitter_model import DocumentWrapper

DEST_DOCS_FOLDER = "DEST_DOCS_FOR_AI"

async def do_text_splitting_with_recursiveCharTextSpliiter(documentWrapper: DocumentWrapper):
    try:
        loader = TextLoader(DEST_DOCS_FOLDER+"\\"+ documentWrapper.document_file_name, encoding="utf-8")
        docs = loader.load()
        print(docs[0].page_content)

        r_splitter = RecursiveCharacterTextSplitter(
            chunk_size=70,
            chunk_overlap=10,
            separators=["\n\n", "\n", " ", ""]
        )
        split_lst = r_splitter.split_documents(docs)
        return {"model_response": len(split_lst)}

    except Exception as e:
        return {"model_response": "Exception Occured!!"}