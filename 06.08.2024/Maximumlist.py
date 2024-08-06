def find_maximum(numbers):
    if not numbers:
        return None
    
    max_value = numbers[0]
    
    for number in numbers:
        if number > max_value:
            max_value = number
    
    return max_value

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"The maximum value in the list is: {find_maximum(numbers)}")
