def calculate_average(numbers):
    if not numbers:
        return None
    total = calculate_sum(numbers)
    return total / len(numbers)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"The average of the list is: {calculate_average(numbers)}")
