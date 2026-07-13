from fastapi import HTTPException

from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
from output_parsers_all_06.model.output_parser_model import ParserModel, Disaster


async def do_sequential_chain_summary(parserModel: ParserModel):
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

async def do_parallel_chain_summary(parserModel: ParserModel):
    try:
        #model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.1)
        model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)
        topic = parserModel.topic
        print(topic)
        template1 = PromptTemplate(
            template="Write a detailed report on {topic}",
            input_variables=["topic"]
        )
        parser = StrOutputParser()

        chain1 = template1 | model | parser
        print("111111111")   

        summary_chain = PromptTemplate(
            template="Write a Summary of the text \n {text}",
            input_variables=["text"]
        )
        print("222222222")   
        quiz_chain = PromptTemplate(
            template="Write 5 questions with answer as quiz from the text \n {text}",
            input_variables=["text"]
        )
        print("3333333")  
        parallel_chain = RunnableParallel ( {
            "summary" : summary_chain | model | parser,
            "quiz" : quiz_chain | model |parser
            }
        )
        prompt_z = PromptTemplate(
            template="Merge the provided summary and quiz into a sinngle document \n summary -> {summary} and quiz -> {quiz}",
            input_variables=["summary", "quiz"]
        )
        print("44444444") 
        final_chain = chain1 | parallel_chain | prompt_z | model | parser
        print("55555554") 
        response = final_chain.invoke({"topic": topic})
        print("6666") 
        print(response)
        return {"model_response": response}
    except Exception as e:
        return {"model_response": "Exception Occred!!"}
