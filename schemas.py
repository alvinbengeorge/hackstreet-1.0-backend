from pydantic import BaseModel

class Input(BaseModel):
    text: str

class Question(BaseModel):
    text: str
    question: str