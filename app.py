from fastapi import FastAPI
from processing import (
    generateFAQ, 
    answerQuestion,
    generateSummary
)
from schemas import (
    Input,
    Question
)

import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Open"}

@app.post("/faq")
def faq(inp: Input):
    return generateFAQ(inp.text)

@app.post("/answer")
def answer(input: Question):
    return answerQuestion(input.text, input.question)

@app.post("/summary")
def summary(input: Input):
    return {"summary": generateSummary(input.text)}

uvicorn.run(app, port=8000)
