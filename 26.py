# Write a program to find the count of maximum occuring character in a string. 

# Constraints: 
# 0 < String length < 100
# Example: 
# Input:
# Hello World
# Output:
# 3
# Explanation: 
# This program allows the user to enter a string (or character array). Next, it will find the maximum 
# occurring character (most repeated character) inside a string

# def max_occuring_char_count(input_string):
#     # Remove spaces and convert the string to lowercase for case-insensitive comparison
#     cleaned_string = input_string.replace(" ", "").lower()

#     # Create a dictionary to store character frequencies
#     char_count = {}

#     # Iterate through the characters in the cleaned string
#     for char in cleaned_string:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1

#     # Find the maximum occurring character and its count
#     max_char = max(char_count, key=char_count.get)
#     max_count = char_count[max_char]

#     return max_count

# # Example Usage:
# user_input = "hi tanishq you know yu are the best"
# result = max_occuring_char_count(user_input)

# print(f"The count of the most frequently occurring character is: {result}")

def max_occuring_char_count(input_string):
    cleaned_s = input_string.replace(" ", "").lower()
    char_count = {}
    for char in cleaned_s:
        if char in char_count:
            char_count[char]+= 1
        else:
            char_count[char] = 1
    max_char = max(char_count , key= char_count.get)
    max_count = char_count[max_char]
    print(max_char)

    return max_count

user_input = input("Enter a string : ")
result = max_occuring_char_count(user_input)
print(result)

# ----------------------------------------------------DONE---------------------------------------------------------------------------------------