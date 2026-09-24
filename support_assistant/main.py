from fastapi import FastAPI
from pydantic import BaseModel

from rag import ask_question, AnswerResponse


app = FastAPI(
    title="Zepto Support Assistant"
)


class AskRequest(BaseModel):
    query: str


@app.post("/ask", response_model=AnswerResponse)
def ask(request: AskRequest):

    return ask_question(request.query)