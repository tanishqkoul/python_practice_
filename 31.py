# Write a programm to print all natural numbers between given range using 
# recursive function .
 

# Constraints: 
# I/P:
# First line reads lower limit
# Second line reads upper limit
# O/p:
# print the natural numbers in a line seperated by space.
# Example: 
# input:
# 1 5
# output:
# 1 2 3 4 5 
 

# Explanation: 
# Base condition of recursive function to print natural numbers is loweLimit < 
# upperLimit. Which is our required condition to return control from function. After 
# checking base condition print the value of lowerLimit and make a recursive call 
# to printNaturalNumbers() function i.e. printNaturalNumbers(lowerLimit + 1, 
# upperLimit);
# def print_natural_numbers(lower_limit, upper_limit):
#     # Base condition to check if lower limit is less than or equal to upper limit
#     if lower_limit <= upper_limit:
#         print(lower_limit, end=" ")  # Print the current natural number
#         print_natural_numbers(lower_limit + 1, upper_limit)  # Recursive call for the next number

# # Example usage:
# lower_limit = 1
# upper_limit = 5

# # Print natural numbers within the specified range
# print("Natural numbers between", lower_limit, "and", upper_limit, "are:")
# print_natural_numbers(lower_limit, upper_limit)


def print_natural_numbers(lower_limit, upper_limit):
    if lower_limit<=upper_limit:
        print(lower_limit, end=" ")
        print_natural_numbers(lower_limit + 1 , upper_limit)

lower_limit= int(input("Enter the lower limit number : "))
upper_limit = int (input("Ener the upper limit number: "))
result = print_natural_numbers(lower_limit, upper_limit)
print(result)

# ----------------------------------------------------------done--------------------------------------------------------------
