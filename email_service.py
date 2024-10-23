import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email, subject, message):
    # Configura tu servidor SMTP (puedes usar Gmail, por ejemplo)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "tucorreo@gmail.com"  # Reemplazar por tu correo
    sender_password = "tu_password"  # Reemplazar por tu contraseña

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Enviar el correo
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Asegura la conexión
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.close()
        print(f"Correo enviado a {to_email}")
    except Exception as e:
        print(f"Error enviando correo: {str(e)}")

# Prueba la función
if __name__ == '__main__':
    send_email("victor.rodriguez_p@mail.udp.cl", "Estado de Pedido", "Tu pedido ha sido enviado.")
