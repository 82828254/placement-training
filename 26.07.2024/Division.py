num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num2 != 0:
    quotient = num1 / num2
    print(f"Quotient: {quotient:.2f}")
else:
    print("Error! Division by zero.")
