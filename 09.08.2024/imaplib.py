import imaplib

def email_login(email, password):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email, password)
    mail.logout()
