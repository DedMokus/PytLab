import random
import socket
import re
import smtplib
import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    dotenv.load_dotenv(dotenv_path)

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

EMAIL_LOGIN_ADMIN = os.getenv("EMAIL_LOGIN_ADMIN")
EMAIL_PASSWORD_ADMIN = os.getenv("EMAIL_PASSWORD_ADMIN")

HOST = "127.0.0.1"
PORT = 22943

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()

    with connection:
        print(f"Connected by {address}")
        while True:
            data = connection.recv(1024)
            if not data:
                break
        Mail, Text = data.split("/")
        if (Mail is None) or (Text is None):
            s.sendall("Error - empty data!")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", Mail):
            s.sendall("Error with Mail address")
        else:
            ID = int(''.join(random.sample('0123456789',5)))
            Subject = "[Ticket #{} Mailer]".format(ID)
            Email = 'Subject: {}\n\n{}'.format(Subject, Text)
            ToEmails = [EMAIL_LOGIN_ADMIN, Mail]
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
                smtp.starttls()
                try:
                    smtp.login(EMAIL_LOGIN_ADMIN, EMAIL_PASSWORD_ADMIN)
                    smtp.sendmail(EMAIL_LOGIN_ADMIN, ToEmails, Email)
                except Exception:
                    s.sendall("Error in sending")
                else:
                    s.sendall("OK")

