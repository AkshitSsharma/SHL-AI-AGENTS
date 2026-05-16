from llm import generate_reply
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from retriever import search_assessments
from intent import detect_intent

app = FastAPI()

# Message schema
class Message(BaseModel):
    role: str
    content: str

# Request schema
class ChatRequest(BaseModel):
    messages: List[Message]

# Health endpoint
@app.get("/health")
def health():

    return {
        "status": "ok"
    }

# Chat endpoint
@app.post("/chat")
def chat(req: ChatRequest):

    latest_message = req.messages[-1].content

    intent = detect_intent(latest_message)

    # Clarification logic
    if intent == "vague":

        return {
            "reply": "What role are you hiring for and what skills are most important?",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Retrieve recommendations
    results = search_assessments(latest_message)
    reply = generate_reply(
    latest_message,
    results
)

    recommendations = []

    for item in results:

        recommendations.append({
            "name": item.get("name"),
            "url": item.get("link"),
            "test_type": "A"
        })

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": False
    }