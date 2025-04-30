from fastapi import FastAPI, Depends
from app.schemas import ChatRequest, ChatResponse
from app.openai_api import ask_openai
from app.database import get_db
from pymongo.database import Database
from datetime import datetime

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, db: Database = Depends(get_db)):
    response_text = ask_openai(request.prompt)

    # Save to MongoDB
    db.history.insert_one({
        "prompt": request.prompt,
        "response": response_text,
        "timestamp": datetime.utcnow()
    })

    return ChatResponse(prompt=request.prompt, response=response_text)
