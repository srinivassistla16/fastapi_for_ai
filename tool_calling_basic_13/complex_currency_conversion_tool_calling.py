import json
import os
from typing import Annotated

from langchain_openai import ChatOpenAI
import requests
from langchain.tools import InjectedToolArg
from langchain_community.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from tool_calling_basic_13.model.tool_call_model import SimpleQuery

EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY", "")
url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/"


@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> dict:
    """This function fetches the currency conversion factor between base_currency and target_currency."""
    response = requests.get(url + base_currency + "/" + target_currency, timeout=10)
    response.raise_for_status()
    return response.json()


@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """This tool calculates the target currency value from the base currency value and conversion rate."""
    return float(base_currency_value) * float(conversion_rate)


# Step 2: bind the tools to the LLM
#llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.9)
llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)
llm_with_tool = llm.bind_tools([get_conversion_factor, convert])

async def do_tool_calling_complex_currency_conversion(simpleQuery: SimpleQuery):
    messages = []
    initial_message = HumanMessage(
        simpleQuery.query_str
    )
    messages.append(initial_message)

    ai_message = llm_with_tool.invoke(messages)
    messages.append(ai_message)
    tool_calls = ai_message.tool_calls
    conversion_rate = 0.0
    for tool_call in tool_calls:
        if tool_call['name'] == 'get_conversion_factor':
            tool_message1 = get_conversion_factor.invoke(tool_call)
            tool_message_content_dict = json.loads(tool_message1.content)
            conversion_rate = tool_message_content_dict['conversion_rate']
            messages.append(tool_message1)
        if tool_call['name'] == 'convert':
            arg1_extn = tool_call['args']['conversion_rate'] = conversion_rate
            print(tool_call['args'])
            tool_message2 = convert.invoke(tool_call)
            messages.append(tool_message2)
    final_answer = llm_with_tool.invoke(messages).content
    return {"model_response": final_answer, "messages": str(messages)}