def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"The sum of the list is: {calculate_sum(numbers)}")
