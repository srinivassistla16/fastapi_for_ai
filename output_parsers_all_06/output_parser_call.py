from fastapi import HTTPException

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from output_parsers_all_06.model.output_parser_model import ParserModel


async def do_str_output_parser_detail(parserModel: ParserModel):
    try:
        model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.1)
        topic = parserModel.topic
        template1 = PromptTemplate(
            input_variables=["topic"],
            template="Write a detailed report on {topic}",
        )
        parser = StrOutputParser()
        chain = template1 | model | parser
        print("Invoking the chain with topic:", topic)
        response = chain.invoke(topic)
        return {"model_response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


async def do_str_output_parser_summary(parserModel: ParserModel):
    try:
        print("STEP 1")
        model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.1)
        topic = parserModel.topic
        template1 = PromptTemplate(
            template="Write a detailed report on {topic}",
            input_variables=["topic"]
        )
        print("STEP 2")
        template2 = PromptTemplate(
            template="Write a 5 lines summary on the following text: /n{text}",
            input_variables=["text"]
        )
        parser = StrOutputParser()
        print("STEP 3")
        chain = template1 | model | parser | template2 | model | parser
        print("STEP 4")
        print("Invoking the chain with topic:", topic)
        response = chain.invoke(topic)
        return {"model_response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
