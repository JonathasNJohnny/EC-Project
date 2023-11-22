import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email():
    # Configurações do servidor SMTP do Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    remetente = "ferreirakaua341@gmail.com"
    senha = "senhaexemplo"  # Substitua com sua senha ou senha de aplicativo
    destinatario = "kauamarques52@outlook.com"

    # Corpo do email em formato HTML
    corpo_email = """
    <p>olá Kauã</p>
    <p>Segue o exemplo de teste de emails automáticos </p>
    """

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

    print('Email enviado com sucesso!')

# Chame a função para enviar o email
enviar_email()
