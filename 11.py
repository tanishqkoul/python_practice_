def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

numbers = [1, 2, 3, 4, 5]
avg = calculate_average(numbers)
print("Average:", avg)

