import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#função para geração de senhas
def gerar_senha(tamanho=8):
  caracteres = string.ascii_letters + string.digits + string.punctuation
  senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
  return senha


def enviar_email():
    # Configurações do servidor SMTP do Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    remetente = "nutrihealth59@gmail.com"
    senha = "hrxb kmpb avnl fyol"  # Substitua com sua senha ou senha de aplicativo
    destinatario = "kauamarques52@outlook.com" #substitua  destinatário pelo usuário que esteja fazendo login


    # Vamos gerar uma senha de 8 caracteres
    senha_gerada = gerar_senha(8)
  
    # Corpo do email em formato HTML
    corpo_email = """
    <p>olá Kauã,</p>
    <p>Segue o exemplo de teste de emails automáticos </p>
    <p>Sua senha é: {}</p>
    """.format(senha_gerada)

    # Criar o objeto MIMEMultipart
    msg = MIMEMultipart()
    msg['Subject'] = "Teste de email"
    msg['From'] = remetente
    msg['To'] = destinatario

    # Adicionar corpo do email ao objeto MIMEMultipart
    msg.attach(MIMEText(corpo_email, 'html'))

    # Iniciar conexão SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Use TLS para segurança

        # Login com suas credenciais
        server.login(remetente, senha)

        # Enviar o email
        server.sendmail(remetente, destinatario, msg.as_string())

    print('Email enviado com sucesso!!')

# Chame a função para enviar o email
enviar_email()
