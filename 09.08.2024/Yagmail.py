import yagmail

def email_login(email, password):
    yag = yagmail.SMTP(email, password)
    yag.close()
