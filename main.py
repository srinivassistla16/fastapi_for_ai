from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from exception_handlers import add_exception_handlers

from models_all_01.routes import router as models_routers
from general_00.routes import router as general_routes
from embeddings_all_02.routes import router as embeddings_routers
from prompting_all_003.routes import router as prompt_call_routers
from chatbot_04.routes import router as chatbot_router
from structured_output_all_05.routes import router as structured_output_router
from output_parsers_all_06.routes import router as output_parsers_routers
from chains_all_07.routes import router as chains_router
from file_uploads.routes import  router as file_upload_router
from document_loaders_all_08.routes import router as document_loader_router
from text_splitter_09.routes import router as text_splitter_router
from vector_store_all_10.routes import router as vector_store_router
from retriever_all_11.routes import router as retriever_router
from custom_tools_12.routes import router as custom_tool_router
from tool_calling_basic_13.routes import router as tool_calling_basic_router

load_dotenv()

# Though the name in env file set as same now , you can keep any other name also in .env file and use that name here to get the value of the key.
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key

google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key:
    os.environ["GOOGLE_API_KEY"] = google_api_key

hf_home = os.getenv("HF_HOME")
if hf_home:
    os.environ["HF_HOME"] = hf_home


app = FastAPI()
add_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(general_routes)
app.include_router(models_routers)
app.include_router(prompt_call_routers)
app.include_router(embeddings_routers)
app.include_router(chatbot_router)
app.include_router(structured_output_router)
app.include_router(output_parsers_routers)
app.include_router(chains_router)
app.include_router(file_upload_router)
app.include_router(document_loader_router)
app.include_router(text_splitter_router)
app.include_router(vector_store_router)
app.include_router(retriever_router)
app.include_router(custom_tool_router)
app.include_router(tool_calling_basic_router)
