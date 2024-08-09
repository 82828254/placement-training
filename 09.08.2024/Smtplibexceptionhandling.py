import smtplib

def email_login(email, password):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
    except smtplib.SMTPAuthenticationError:
        print("Failed to login")
    finally:
        server.quit()
