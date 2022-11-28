import imaplib
import email
import os
import base64
import shutil

def getPDFinEmail():
    emails = imaplib.IMAP4_SSL("imap.gmail.com")
    login = "machinesdotcom@gmail.com"
    senha = "djvvnmeequtisdoq"

    emails.login(login, senha)

    emails.list()
    emails.select(mailbox='inbox', readonly=True)

    resp, idEmail = emails.search(None, 'All')

    for i in idEmail[0].split():
        resultado, dados = emails.fetch(i, '(RFC822)')
        emailText = dados[0][1]
        emailText = emailText.decode('UTF-8')
        emailText = email.message_from_string(emailText)

        for em in emailText.walk():
            if em.get_content_maintype() == 'multipart':
                continue
            if em.get('Content-Disposition') is None:
                continue
            nomeArq = em.get_filename()
            if (nomeArq.__contains__('.pdf')):
                arquivo = open(nomeArq, 'wb')
                arquivo.write(em.get_payload(decode=True))
                arquivo.close()

class RequestEmail:
    pass

