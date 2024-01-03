# Write a program to display the missing number in a consecutive 1 to n
# numbers in a list
# Example:
# Input:
# 10 1 2 3 4 5 6 8 9 

# 10
# Output:
# 7
# Input:
# 1 2 3 4 6 7 8 9
# 9
# Output:
# 5
# Explanation:
# 1st line of the input is 1 to 9 consecutive numbers with one missing number
# 1st line of the output is that 1 missing number in that list

# def find_missing_number(numbers, n):
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(numbers)
#     missing_number = expected_sum - actual_sum
#     return missing_number

# # Example usage:
# input_numbers = [10, 1, 2, 3, 4, 5, 6, 8,9]
# n1 = 10
# result1 = find_missing_number(input_numbers, n1)
# print("Output:", result1)

# input_numbers2 = [1, 2, 3, 4, 6, 7, 8, 9]
# n2 = 9
# result2 = find_missing_number(input_numbers2, n2)
# print("Output:", result2)


def Find_missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    missing_number = expected_sum - actual_sum

    return missing_number


n1 = int(input("Enter total number : "))
input_numbers = input(f"Enter the numbers from zero to  {n1} seprated by spaces :")
numbers_list = list(map(int,input_numbers.split()))

result = Find_missing_number(numbers_list, n1)
print(f"The missing no is : {result}")
# ----------------------------------------------------------DONE-------------------------------------------------------------------------------

                    
