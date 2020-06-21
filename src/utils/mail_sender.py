import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "simplebot80@gmail.com"
password = "fabcaa97871555b68aa095335975e613"

context = ssl.create_default_context()


def send_mail_login(receiver, code):
    receiver_email = receiver
    message = f"""Subject: Intento de Login

       Hola, {receiver.split("@")[0]}
       
       Hubo un intento de Login en nuestro sistem de encriptación.

        Para realizar el Login de manera exitosa ingrese el siguiente código:

       {code}

       El código expirará en 5 minutos.

       Gracias ^^ ."""

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        print(f"sending mail to {receiver_email}")
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
