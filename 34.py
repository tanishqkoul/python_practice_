# write a program to accept a string and print an individual sub-string with its
# length.
# Example:
# Input:
# hello buddy
# Output:
# hello 5
# buddy 5


# def print_substring_lengths(input_string):
#     words = input_string.split()

#     for word in words:
#         print(f"{word} {len(word)}")

# # Example usage:
# input_str = "hello buddy"
# print_substring_lengths(input_str)

def  print_substrings_length(input_string):
    words = input_string.split()

    for word in words:
        print(f"{word} {len(word)}")

input_string = input("Enter the string :")
result = print_substrings_length(input_string)
print(result)

# ---------------------------------------------------DONE----------------------------------------------------------------------
