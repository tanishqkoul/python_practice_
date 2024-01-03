# You are tasked with writing a function to calculate the factorial of a non-negative integer n. The 
# factorial of a number n is the product of all positive integers less than or equal to n. It is denoted by n! and is defined as:
# n!=n×(n−1)×(n−2)×…×2×1
# Write a function to calculate the factorial of a non-negative integer n where 0≤n≤20.
# Ensure that your solution runs in O(n) time complexity and uses O(1) space.
# If n is negative then print -1. 

# Constraints: 
# 1. Input Limits: ◦ The input number is within a specific range, e.g., 0 to 20.
# 1. Output Limits: ◦ The result should fit within a certain data type (e.g., 32-bit integer). 1. Time Complexity: ◦ Your solution must execute within a specified time limit, such as O(n), where n is the input 
# number.
# 1. Space Complexity: ◦ There may be restrictions on the amount of memory your solution can use, expressed in terms 
# of space complexity.
# Example: 
# I/p:
# 5
# O/p:
# 120
# Explanation: 
# For n=5
# Logic is 5*4*3*2*1
# So it is 120

def factorial(n):
    if n < 2:
        return -1
    
    result = 1
    for i in range(1, n+1):
        result *= i
        print(i)
    return result

n = 10
result = factorial(n)
print(result)
# ---------------------------------------------DONE--------------------------------------------------------------------