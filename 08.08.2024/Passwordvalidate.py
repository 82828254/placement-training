def validate_password(password):
    if len(password) < 8:
        return "Password too short!"
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit!"
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter!"
    return "Password is valid!"

password = input("Enter your password: ")
print(validate_password(password))
