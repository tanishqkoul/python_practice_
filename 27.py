# Write a program to find Absolute difference between number of vowels and consonants in a given 
# string.
# Constraints: 
# 0 < string length < 100
# Example: 
# Input:
# instacks
# Output:
# 4
# 1<=|S|<=105
# 1<=|pat|<|S|
# Input 1: batmanandrobinarebat
# bat
# output: 1 18
# Explanation: 
# • The string "instacks" has 2 vowels ('i', 'a') and 6 consonants ('n', 's', 't', 'c', 'k', 's').
# • The absolute difference between the number of vowels and consonants is ∣2−6∣=4∣2−6∣=4, 
# which is the output.def find_absolute_difference(input_string):
# Function to check if a character is a vowel

# def find_absolute_difference(input_string):
#     # Function to check if a character is a vowel
#     def is_vowel(char):
#         return char.lower() in ['a', 'e', 'i', 'o', 'u']

#     # Initialize counters for vowels and consonants
#     vowel_count = 0
#     consonant_count = 0

#     # Iterate through each character in the input string
#     for char in input_string:
#         # Check if the character is a vowel
#         if is_vowel(char):
#             vowel_count += 1
#         else:
#             consonant_count += 1

#     # Calculate the absolute difference between the counts
#     absolute_difference = abs(vowel_count - consonant_count)

#     return absolute_difference

# # Example usage:
# input_str = "instacks"
# result = find_absolute_difference(input_str)
# print(result)

# input_str2 = "batmanandrobinarebat"
# result2 = find_absolute_difference(input_str2)
# print(result2)
def find_absolute_difference(input_string):
    def is_vovel(char):
        return char.lower() in ['a', 'e' , 'i', 'o', 'u']
    
    vovel_count = 0
    consonant_count = 0 

    for char in input_string:
        if is_vovel(char):
            vovel_count+=1
        else:
            consonant_count+=1

    absolute_difference = abs(vovel_count - consonant_count)
    return absolute_difference

input_string = input("Enter the string :")
result = find_absolute_difference(input_string)
print(result)
 
# ---------------------------------------------------------------------DONE-----------------------------------------------------------------------------