from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path
from enviar_form import enviar_email  # Importa a função de envio de e-mail

app = FastAPI()

# Monta arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura os diretórios de templates
templates = Jinja2Templates(directory="pages")

# Rota para a página inicial (index.html)
@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota para o formulário (orcamento.html)
@app.get("/orcamento.html", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("orcamento.html", {"request": request})

# Rota para processar o formulário e enviar o e-mail
@app.post("/enviar_orcamento", response_class=HTMLResponse)
async def enviar_orcamento(
    request: Request,
    nome: str = Form(...),
    fone: str = Form(...),
    fone2: str = Form(None),
    email: str = Form(...),
    mensagem: str = Form(...),
    fotos: list[UploadFile] = File(None)
):
    # Salva os arquivos temporariamente se houver
    fotos_salvas = []
    if fotos:
        for foto in fotos:
            foto_path = f"temp_{foto.filename}"
            with open(foto_path, "wb") as f:
                f.write(foto.file.read())
            fotos_salvas.append(foto_path)

    # Chama a função de enviar o e-mail (do arquivo enviar_form.py)
    try:
        enviar_email(nome, fone, fone2, email, mensagem, fotos=fotos_salvas)
        # Apaga os arquivos temporários após o envio
        for foto_path in fotos_salvas:
            os.remove(foto_path)
        return HTMLResponse(content="<h1>Formulário enviado com sucesso!</h1>", status_code=200)
    except Exception as e:
        return HTMLResponse(content=f"<h1>Erro ao enviar o formulário: {e}</h1>", status_code=500)
