import smtplib
import email.message
from senha import senha


def enviar_email():
    faturamento = 1000
    corpo_email = f"""
    <p>Prezados,</p>
    <p>Segue meu primeiro email automatico</p>
    <p>faturamento do mes foi R${faturamento}</p>
    <p>abs</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Email automatico"
    msg['From'] = 'email'
    msg['To'] = 'email'
    password = senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()


