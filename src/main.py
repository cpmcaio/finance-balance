from fastapi import FastAPI
from .api.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def hello_word():
    return {"message":"hello world"}