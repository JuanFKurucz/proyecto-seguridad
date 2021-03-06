import smtplib, ssl

from src.utils.config import EMAIL_USERNAME, EMAIL_PASSWORD

smtp_server = "smtp.gmail.com"
port = 587
context = ssl.create_default_context()


def send_mail_login(receiver, code):
    receiver_email = receiver
    message = f"""Subject: Intento de Login

       Hola, {receiver}
       
       Hubo un intento de Login en nuestro sistem de encriptacion.

       Para realizar el Login de manera exitosa ingrese el siguiente codigo:

       {code}

       El codigo expirara en 5 minutos.

       Gracias ^^ ."""

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        print(f"Enviando token de conexion al mail del usuario")
        server.sendmail(EMAIL_USERNAME, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
