from transformers import pipeline,logging
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

logging.set_verbosity_error()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',            # TODO уязвимость безопасности, в будущем указать разрешенные источники
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipe = pipeline("text-generation", model="openai-community/gpt2")

class TextIn(BaseModel):
    prompt: str

class TextOut(BaseModel):
    answer: str

@app.get("/info")
async def boot():
    return {'model_status':'ready', 'API_version': '0.0.1'}

@app.post('/request', response_model=TextOut)
async def request(payload: TextIn):
    answer = pipe(payload.prompt)[0]['generated_text']
    return {'answer': answer}

app.mount('/', StaticFiles(directory='static',html=True), name='static')