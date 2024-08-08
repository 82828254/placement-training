import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_+="
    return ''.join(random.choice(characters) for _ in range(length))

length = int(input("Enter the length of the password: "))
print("Generated password:", generate_password(length))
