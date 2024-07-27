import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
lcm = abs(num1 * num2) // math.gcd(num1, num2)
print(f"LCM: {lcm}")
