def find_maximum(numbers):
    max_number = 0
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

# Test the function
numbers_to_test = [3, 7, 1, 15, 40, 12]
result = find_maximum(numbers_to_test)

print(f"The maximum number is: {result}")
