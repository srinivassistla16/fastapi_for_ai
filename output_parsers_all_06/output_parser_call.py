from fastapi import HTTPException

from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from output_parsers_all_06.model.output_parser_model import ParserModel, Disaster, Sentiment


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
        #model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.1)
        model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)
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


async def do_json_output_parser_summary(parserModel: ParserModel):
    try:
        model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.1)
        topic = parserModel.topic
        json_parser = JsonOutputParser(pydantic_object= Disaster)
        template1 = PromptTemplate(
        template="Write disaster name, cause, effect and precautions for the following disaster \n {format_instructions} \n {topic}",
            input_variables=["topic"],
            partial_variables={"format_instructions": json_parser.get_format_instructions()}
        )
        chain = template1 | model | json_parser
        print("Invoking the chain with topic:", topic)
        response = chain.invoke(topic)
        return {"model_response": str(response)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


async def do_pydantic_output_parser_sentiment(parserModel: ParserModel):
    model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)
    #model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.1)
    topic = parserModel.topic
    print("00000 "+ topic)
    pydantic_parser = PydanticOutputParser(pydantic_object= Sentiment)
    template1 = PromptTemplate(
        template="Classify the following statement with sentiment analysis of POSITIVE, NEGATIVE \n {format_instructions} \n {topic}",
        input_variables=["topic"],
        partial_variables={"format_instructions": pydantic_parser.get_format_instructions()}
    )
    
    chain = template1 | model | pydantic_parser
    print("Invoking the chain with topic:", topic)
    response = chain.invoke(topic)
    print("11111 "+ str(response))
    ai_positive_promt = PromptTemplate(
        template = "Provide the suitable ai response to the following statement\n {statement} ",
        input_variables=["statement"]
    )

    ai_negive_promt = PromptTemplate(
        template = "Provide the suitable ai response to the following statement\n {statement} ",
        input_variables=["statement"]
    )
    str_parser = StrOutputParser()
    
    print("CONSTRUCTING FINAL CHAIN")
    branch_chain = RunnableBranch(
        (lambda x: x.sentiment == 'POSITIVE' ,ai_positive_promt | model | str_parser ),
        (lambda x: x.sentiment == 'NEGATIVE' ,ai_negive_promt | model | str_parser ),
        RunnableLambda(lambda x: "Sorry , No Sentiment")
    )
    print("STARTED... final invoke")
    final_chain = chain | branch_chain
    airesponse = final_chain.invoke(topic)
    return {"model_response": response.sentiment, "ai_response": airesponse}
