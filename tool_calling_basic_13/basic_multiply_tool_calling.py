from langchain_community.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

from tool_calling_basic_13.model.tool_call_model import SimpleQuery

@tool
def multiply(num1: int, num2: int) -> int:
    """"Given two numbers num1 and num2, this tool returns their product"""
    return num1 * num2

#step2: bind this tool to an llm
llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.9)
llm_with_tool = llm.bind_tools([multiply])


async def do_tool_calling_for_multiplier(simpleQuery: SimpleQuery):
    messages = []
    human_message = HumanMessage(simpleQuery.query_str)
    messages.append(human_message)

    ai_message = llm_with_tool.invoke(messages)
    messages.append(ai_message)
    tool_calls_as_input = ai_message.tool_calls[0]

    tool_message = multiply.invoke(tool_calls_as_input)
    messages.append(tool_message)

    parser = StrOutputParser()

    chain = llm_with_tool | parser
    
    final_answer = chain.invoke(messages)

    return {"model_response": final_answer, "messages": str(messages)}