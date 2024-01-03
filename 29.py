# Write a program to generate and print a dictionary that contains a number (between 1 and n) in 
# square form. Constraints: 
# n>0
# Example: 
# I/p:
# 5
# O/p:
# {1:1,2:4,3:9,4:16,5:25}
# Explanation: 
# I/p:
# Take the input as integer from the user
# O/p: For that we have to print in dictioanary as key from the number and the value as its square
# def generate_square_dictionary(n):
#     square_dict = {}

#     for num in range(1, n+1):
#         square_dict[num] = num ** 2

#     return square_dict

# # Example usage:
# user_input = int(input("Enter a number (n): "))
# result_dict = generate_square_dictionary(user_input)
# print(result_dict)

def generate_square_dictionary(n):
    square_dict = {}

    for num in range(1, n+1):
        square_dict[num] = num ** 2

    return square_dict

user_input = int(input("Enter a number(n): "))
result = generate_square_dictionary(user_input)
print(result) 



# ---------------------------------------------------------DONE--------------------------------------------------------------------------