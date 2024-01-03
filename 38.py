# Write a program to create a new string made of the middle three characters
# of an input string
# Input: 
# Annamacharya
# Output: 
# ach
# Explanation: 
# Get the middle character’s index using x = len(str1) /2.
# Use string slicing to get the middle three characters starting from the middle index 
# to the next two character str1[middle_index-1:middle_index+2
                               
# def get_middle_three_chars(input_str):
#     middle_index = len(input_str) // 2

#     # Use string slicing to get the middle three characters
#     middle_three_chars = input_str[middle_index - 1: middle_index + 2]

#     return middle_three_chars

# # Example usage:
# input_string = "Annamacharya"
# result = get_middle_three_chars(input_string)
# print("Output:", result)


def Middle_three_chars(input_str):
    middle_index = len(input_str) // 2

    middle_three_chars = input_str[middle_index -1 : middle_index+2]

    return middle_three_chars

input_str = "Tanishq"
result = Middle_three_chars(input_str)
print(result)

# ----------------------------------------------------DONE--------------------------------------------------------------------
