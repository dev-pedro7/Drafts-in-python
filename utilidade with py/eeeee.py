import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP do Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'thing10@gmail.com'
smtp_password = 'password'

# Configurações do e-mail
sender_email = 'any'
receiver_email = 'any@gmail.com'
subject = 'Assunto do e-mail'
body = 'Corpo do e-mail'

# Criando a mensagem
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Adicionando o corpo do e-mail
message.attach(MIMEText(body, 'plain'))

# Conectando ao servidor SMTP do Gmail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Inicia uma conexão segura
    server.login(smtp_username, smtp_password)  # Faz login no servidor

    # Enviando o e-mail
    server.sendmail(sender_email, receiver_email, message.as_string())

print('E-mail enviado com sucesso!')
