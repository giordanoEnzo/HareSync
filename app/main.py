from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import chat, administrador


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(administrador.router)