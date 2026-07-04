from tempfile import template

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_openai import ChatOpenAI
from prompting_all_003.model.prompt_data_model import PromptDataModel

async def do_promptcall_using_datamodel_openai(promptDataModel: PromptDataModel):
    prompt = getPromptValue(promptDataModel)
    print("Prompt Generated is : ", prompt)
    llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)
    response = llm.invoke(prompt)
    return {"model_response" : response.content}

async def do_promptcall_using_datamodel_gemini(promptDataModel: PromptDataModel):
    prompt = getPromptValue(promptDataModel)
    print("Prompt Generated is : ", prompt)
    llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.9)
    response = llm.invoke(prompt)
    return {"model_response" : response.content[0].get("text")}

async def do_promptcall_using_datamodel_huggingface(promptDataModel: PromptDataModel):
    prompt = getPromptValue(promptDataModel)
    llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v0.6",
    task="text-generation",
    pipeline_kwargs= dict(
        temperature = 0.1,
        max_new_tokens = 1000
    ))
    model = ChatHuggingFace(llm=llm)
    response = model.invoke(prompt)
    return {"model_response" : response.content}

def getPromptValue(promptDataModel: PromptDataModel):
    template = PromptTemplate(
    template= """
    Describe {character_input} character in Indian Mythology {mythology_input} in {no_of_lines_input}  sentences
    """, 
    input_variables=['character_input', 'mythology_input','no_of_lines_input'],
    validate_template=True
    )
    prompt = template.invoke(
    {
        "character_input": promptDataModel.character_input,
        "mythology_input": promptDataModel.mythology_input,
        "no_of_lines_input": promptDataModel.no_of_lines_input
    }
    )
    return prompt