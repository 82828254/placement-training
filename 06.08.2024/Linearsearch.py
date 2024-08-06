def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 5
print(f"Index of {target} in the list: {linear_search(numbers, target)}")
