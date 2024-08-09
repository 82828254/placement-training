import poplib

def email_login(email, password):
    server = poplib.POP3_SSL('pop.gmail.com')
    server.user(email)
    server.pass_(password)
    server.quit()
