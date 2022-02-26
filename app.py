from datetime import datetime
from typing import Optional
import httpx
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import models
import json
import random

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def index(request: Request, username: str = None):
    if not username:
        return templates.TemplateResponse("index.html", context={"request": request})

    user = get_github_profile(request, username)

    context = {"request": request, "user": user}

    return templates.TemplateResponse("index.html", context=context)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/quotes/")
async def get_quote():
    text_file = open("quotes.json", "r")
    data = json.load(text_file)
    
    # data = text_file.read()    
    text_file.close()
    
    return data

class Message:
  def __init__(self, message, author):
    self.message = message
    self.author = author

def mapMessage(item):
    return Message(item['quote'], item['author'])

@app.get("/quote/")
async def get_quote():
    text_file = open("quotes.json", "r")
    data = json.load(text_file)
    text_file.close()
    result = list(map(mapMessage, data['quotes']))
    # return data
    return random.choice(result)


@app.get("/{username}", response_model=models.GithubUserModel)
def get_github_profile(request: Request, username: str) -> Optional[models.GithubUserModel]:

    headers = {"accept": "application/vnd.github.v3+json"}

    response = httpx.get(f"https://api.github.com/users/{username}", headers=headers)

    if response.status_code == 404:
        return False

    user = models.GithubUserModel(**response.json())

    # Sobreescribir la fecha con el formato que necesitamos
    user.created_at = datetime.strptime(user.created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%y")

    return user

