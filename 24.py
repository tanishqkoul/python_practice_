# Write a function that finds the sum of proper divisors of a number. Proper divisors of a number are those numbers by which the number is divisible, except the number itself.
# Constraints: 
# num>0
# Example: 
# proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18 . 

# sum of divisors 55. 
# Explanation: 
# 1.write a function that accept a integer.
# 2.take a empty list.
# 3.run a loop to check wheather the given num is a proper divisor or not.
# 4.now add that proper divisor to list.
# 5.find the sum of the list.
# 6.return the sum

# def Accept_integer(num):
#     divisor = []
#     for i in range(1, num):
#         if num%i == 0:
#             divisor.append(i)
#             print(divisor)
#     return sum(divisor)

# n = 36
# result = Accept_integer(n)
# print(result) 
def Accept_integer(num):
    divisor = []
    for i in range(1, num):
        if num % i == 0 :
            divisor.append(i)
            print(divisor)
    return sum(divisor)

n = int(input("Enter the value: "))
result = Accept_integer(n)
print(result)
# --------------------------------------------------DONE-----------------------------------------------------------------