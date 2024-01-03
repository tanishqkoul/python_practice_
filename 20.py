# Program that takes the 3 numbers and finds the largest number Aamong three numbers.
# Constraints: 
# The program assumes that the input numbers are integers between in range 1 to 10^3.
# Example: 
# Input: 
# 15 12 33
# Output:
# The 3rd Number is the greatest among three.
# input 1: 
# 33 15 12
# output 1: 
# The 1st Number is the greatest among three. 

# input 2: 
# 15 33 12
# output 2: 
# The 2nd Number is the greatest among three 

# Explanation: 
# 1. Take the three numbers as input and store them in variables.
# 2. Check the first number if it is greater than other two.
# 3. Repeat the step 2 for other two numbers.
# 4. Print the number which is greater among all and exit

num1 = int(input("enter the number of your choice : "))
num2 = int(input("enter the number of your choice : "))
num3 = int(input("enter the number of your choice : "))


if num1>num2 and num1>num3:
    print("\nThe no 1ST is the greatest among the three!")
elif num2>num1 and num2>num3:
    print("\nThe no 2nd is the greatest among the three!")
else:
    print("\nThe no 3rd is the greatest among the three!")
