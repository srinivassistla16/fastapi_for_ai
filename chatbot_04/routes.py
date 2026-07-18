from fastapi import APIRouter, HTTPException
from langchain_core.messages import HumanMessage
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

from chatbot_04.model.chat_request_model import ChatRequest

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

router = APIRouter()



# Use the Google Gemini model. GOOGLE_API_KEY is loaded from .env in main.py
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.9)

# Setup the conversational prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful and concise conversational AI assistant. You remember the context of the conversation."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

chain = prompt | model

def get_session_history(session_id: str):
    # This will create 'chat_memory.db' in the project root if it doesn't exist
    return SQLChatMessageHistory(
        session_id=session_id,
        connection="sqlite:///chat_memory.db"
    )

# Wrap the chain with message history
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

@router.post("/api/chatbot/langchain")
async def chat_endpoint(req: ChatRequest):
    try:
        response = chain_with_history.invoke(
            {"input": req.message},
            config={"configurable": {"session_id": req.session_id}}
        )
        return {"model_response" : response.content[0].get("text")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
############################################################

# --- LangGraph Setup ---
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": [response]} # Append the new message to state

builder = StateGraph(MessagesState)
builder.add_node("model", call_model)
builder.add_edge(START, "model")

memory = MemorySaver()
graph = builder.compile(checkpointer=memory)

@router.post("/api/chatbot/langgraph")
async def chat_endpoint(req: ChatRequest):
    try:
        config = {"configurable": {"thread_id": req.session_id}}
        # Invoke the graph synchronously (or use await graph.ainvoke)
        # We pass the input structured for MessagesState
        final_state = graph.invoke(
            {"messages": [HumanMessage(content=req.message)]}, 
            config=config
        )
        # Extract the last message from the updated MessagesState array
        last_message = final_state["messages"][-1]
        return {"model_response" : last_message.content[0].get('text')}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 


