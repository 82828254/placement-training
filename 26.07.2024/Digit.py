num = int(input("Enter an integer: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print(f"Sum of digits: {sum}")
