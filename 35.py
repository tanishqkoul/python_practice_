# Write a recursive function to generate nth fibonacci term .
# Constraints: 
# • 1 <= n <= 102
# Example: 
# input:
# 10
# output:
# 55
# Explanation: 
# The recursive function to find nth Fibonacci term is based on below three 
# conditions.
# 1. If num == 0 then return 0. Since Fibonacci of 0th term is 0.
# 2. If num == 1 then return 1. Since Fibonacci of 1st term is 1.
# 3. If num > 1 then return fibo(num - 1) + fibo(n-2). Since Fibonacci of a term is 
# sum of previous two terms.
# in given example the 10th term fibonacci is 55

# def fibonacci(n):
#     # Base conditions
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         # Recursive case: Fibonacci of a term is the sum of the previous two terms
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # Example usage:
# user_input = 10

# # Output: Print the nth Fibonacci term
# result = fibonacci(user_input)
# print(result)

def febonacci(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:
        return febonacci( n-1) + febonacci(n-2)
    
user_input = int(input("enter the numbers :"))
result = febonacci(user_input)
print(result)

# ------------------------------------------------------DONE----------------------------------------------------------------------