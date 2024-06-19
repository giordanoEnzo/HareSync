from pydantic import BaseModel

class Prompt(BaseModel):
    cliente: str
    token: str
    pergunta: str
