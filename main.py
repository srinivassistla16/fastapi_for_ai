from fastapi import FastAPI, HTTPException
import os
from dotenv import load_dotenv
load_dotenv()
# Though the name in env file set as same now , you can keep any other name also in .env file and use that name here to get the value of the key.
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key

google_api_key = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = google_api_key

hf_home = os.getenv("HF_HOME")
os.environ["HF_HOME"] = hf_home



from models_all_01.routes import router as models_routers
from general_00.routes import router as general_routes


app = FastAPI()
app.include_router(general_routes)
app.include_router(models_routers)



