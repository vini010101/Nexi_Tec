from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from fastapi import APIRouter, Form, UploadFile, File
from dotenv import load_dotenv
import os

load_dotenv()  # Carregar variáveis de ambiente do .env

router = APIRouter()  # Definindo o roteador

@router.post("/submit")
async def submit_form(
    nome: str = Form(...),
    fone: str = Form(...),
    fone2: str = Form(None),
    email: str = Form(...),
    mensagem: str = Form(...),
    fotos: UploadFile = File(None)
):
    message = Mail(
        from_email='seu_email@dominio.com',
        to_emails='seu_email@dominio.com',  # O mesmo e-mail para onde você deseja enviar
        subject=f'Novo Orçamento de {nome}',
        plain_text_content=f"""
        Nome: {nome}
        Telefone 1: {fone}
        Telefone 2: {fone2}
        E-mail: {email}
        Mensagem: {mensagem}
        """,
    )
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))  # Use a chave da API do SendGrid do .env
        response = sg.send(message)
        return {"message": "Orçamento enviado com sucesso!"}
    except Exception as e:
        return {"error": str(e)}
