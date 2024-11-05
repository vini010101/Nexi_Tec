from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

# Monta arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura os diretórios de templates
templates = Jinja2Templates(directory="pages")

class FormData(BaseModel):
    nome: str
    idade: int
    endereco: str
    email: str
    escolaridade: str
    concordo: bool
    trabalho: str
    mensagem: str

# Rota para a página inicial (index.html)
@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota para o formulário (orcamento.html)
@app.get("/orcamento.html", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("orcamento.html", {"request": request})
