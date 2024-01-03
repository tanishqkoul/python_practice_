# Write a Python program to convert a list into a nested dictionary of keys.
# Input: 
# 4
# 12
# 14
# 15
# 16
# Output: 
# {12: {14: {15: {16: {}}}}}

# def convert_to_nested_dict(numbers):
#     nested_dict = {}
#     current_dict = nested_dict

#     for num in numbers:
#         current_dict[num] = {}
#         current_dict = current_dict[num]

#     return nested_dict

# # Example usage:
# input_numbers = [14, 172, 914, 185, 916]
# result_dict = convert_to_nested_dict(input_numbers)

# print(result_dict)

def convert_to_nested_dict(numbers):
    nested_dict = {}
    current_dict = nested_dict

    for num in numbers:
        current_dict[num] = {}
        current_dict = current_dict[num]

    return nested_dict

input_numbers = input("Enter the numbers in the dictonary :")
numbers_list = list(map(int,input_numbers.split()))
result = convert_to_nested_dict(numbers_list)
print(result)
# -------------------------------------------------------DONE------------------------------------------------------------------