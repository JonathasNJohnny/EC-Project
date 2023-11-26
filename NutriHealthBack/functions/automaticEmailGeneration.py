import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from functions.generateRandomPassword import generatePassword


def sendEmail(name, email):
    # Configurações do servidor SMTP do Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    password = "hrxb kmpb avnl fyol"
    sender = "nutrihealth59@gmail.com"
    receiver = email

    userPassword = generatePassword()
  
    # Corpo do email em formato HTML
    emailBody = f"""
    <p>olá {name},</p>
    <p>Seja bem vindo ao NutriHealth! </p>
    <p>Sua senha gerada é: {userPassword}</p>
    """

    # Criar o objeto MIMEMultipart
    msg = MIMEMultipart()
    msg['Subject'] = "NutriHealth, Boas Vindas!"
    msg['From'] = sender
    msg['To'] = receiver

    # Adicionar corpo do email ao objeto MIMEMultipart
    msg.attach(MIMEText(emailBody, 'html'))

    # Iniciar conexão SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Use TLS para segurança

        # Login com suas credenciais
        server.login(sender, password)

        # Enviar o email
        server.sendmail(sender, receiver, msg.as_string())

    print('Email successfully sent!!')
    return userPassword