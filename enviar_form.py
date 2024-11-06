# enviar_form.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def enviar_email(nome, fone, fone2, email, mensagem, fotos=None):
    # Configurações do servidor SMTP
    server_smtp = "smtp.gmail.com"
    port = 587
    sender_email = os.getenv('EMAIL_REMETENTE')
    password = os.getenv('EMAIL_SENHA_APP')
    recive_email = os.getenv("EMAIL_DESTINATARIO")
    subject = "Novo orçamento"
    
    # Configurando o corpo do e-mail
    body = f"""
    <h1>Orçamento Solicitado</h1>
    <p><strong>Nome:</strong> {nome}</p>
    <p><strong>Telefone 1:</strong> {fone}</p>
    <p><strong>Telefone 2:</strong> {fone2}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Mensagem:</strong> {mensagem}</p>
    """

    # Cria o objeto de mensagem
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recive_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    # Adicionando anexo (caso tenha fotos)
    if fotos:
        for foto in fotos:
            attachment = open(foto, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={foto}')
            msg.attach(part)

    # Enviar o e-mail
    try:
        with smtplib.SMTP(server_smtp, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, recive_email, msg.as_string())
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
