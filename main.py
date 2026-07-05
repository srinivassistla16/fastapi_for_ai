from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

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

from models_all_01.routes import router as models_routers
from general_00.routes import router as general_routes

from embeddings_all_02.routes import router as embeddings_routers
from prompting_all_003.routes import router as prompt_call_routers
from chatbot_01.routes import router as chatbot_router
from exception_handlers import add_exception_handlers

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







