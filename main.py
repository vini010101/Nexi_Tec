from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from enviar_form import router as form_router  # Importa o roteador do enviar_form

app = FastAPI()

# Monta arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura os diretórios de templates
templates = Jinja2Templates(directory="pages")

# Inclui as rotas do enviar_form
app.include_router(form_router)  # Inclui as rotas do roteador

# Rota para a página inicial (index.html)
@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota para o formulário (orcamento.html)
@app.get("/orcamento.html", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("orcamento.html", {"request": request})
