import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = input("Enter your password: ")
hashed_password = hash_password(password)
print("SHA-256 Hashed Password:", hashed_password)
