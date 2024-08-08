def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char in "!@#$%^&*()-_+=" for char in password):
        score += 1

    if score <= 2:
        return "Weak Password"
    elif score == 3:
        return "Moderate Password"
    else:
        return "Strong Password"

password = input("Enter your password: ")
print(check_strength(password))
