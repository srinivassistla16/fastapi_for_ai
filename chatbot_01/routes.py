from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    message: str

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

@router.post("/api/chatbot/google")
async def chat_endpoint(req: ChatRequest):
    try:
        response = chain_with_history.invoke(
            {"input": req.message},
            config={"configurable": {"session_id": req.session_id}}
        )
        return {"model_response" : response.content[0].get("text")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
