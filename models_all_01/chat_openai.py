from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_openai import ChatOpenAI
from models_all_01.model.prompt_query import SimpleQuery
# gpt-4.1-nano


def do_simple_invoke_openai(simpleQuery: SimpleQuery):
    model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)
    query_str = simpleQuery.query_str
   # response = model.invoke("Write 5 lines summary notes of Andhra Pradesh polytics")
    response = model.invoke(query_str)
    return {"model_response" : response.content}

def do_simple_invoke_gemini(simpleQuery: SimpleQuery):
    model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.1)
    query_str = simpleQuery.query_str
    response = model.invoke(query_str)
    return {"model_response" : response.content[0].get("text")}

def do_simple_invoke_huggingface(simpleQuery: SimpleQuery):
    llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v0.6",
    task="text-generation",
    pipeline_kwargs= dict(
        temperature = 0.1,
        max_new_tokens = 1000
    ))
    model = ChatHuggingFace(llm=llm)
    query_str = simpleQuery.query_str
    response = model.invoke(query_str)
    return {"model_response" : response.content}
