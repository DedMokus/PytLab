import base64
import os
import sys
import time

import dotenv
import imaplib
import email
from email.header import decode_header
import re

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    dotenv.load_dotenv(dotenv_path)

success_file = open("success_request.log", "a", encoding="utf-8")
error_file = open("error_request.log", "a", encoding="utf-8")

IMAP_HOST = os.getenv("IMAP_HOST")
IMAP_PORT = int(os.getenv("IMAP_PORT"))
EMAIL_LOGIN_ADMIN = os.getenv("EMAIL_LOGIN_ADMIN")
EMAIL_PASSWORD_ADMIN = os.getenv("EMAIL_PASSWORD_ADMIN")
PERIOD_CHECK = int(os.getenv("PERIOD_CHECK"))

while True:
    print("Cycle on")
    with imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT) as imap:
        imap.login(EMAIL_LOGIN_ADMIN, EMAIL_PASSWORD_ADMIN)
        imap.select("INBOX")

        res, messages = imap.search(None, "UNSEEN")
        #print(messages[0].decode().split(" ")[0])
        if messages[0]:
            res, msg = imap.fetch(messages[0].decode().split(" ")[0], "(RFC822)")
            # res, msg = imap.fetch("141", "(RFC822)")
            msg = email.message_from_bytes(msg[0][1])
            msgSubject = decode_header(msg["Subject"])[0][0]
            if re.match(r"Ticket #\d{5} Mailer", msgSubject):
                ID = re.search(r'#(.+?) ', msgSubject).group()[slice(1, 6)]
                for part in msg.walk():
                    if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
                        text = part.get_payload()
                # sys.stdout.flush()
                #print("Success write")
                success_file.write('Message {}, {}'.format(ID, text))
                success_file.flush()
            else:
                for part in msg.walk():
                    if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
                        text = part.get_payload()
                # sys.stdout.flush()
                #print("Error write")
                error_file.write('Message text: {}'.format(text))
                error_file.flush()
    print("period")
    time.sleep(PERIOD_CHECK)
