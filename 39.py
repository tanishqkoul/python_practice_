# You have a non-empty set s, and you have to execute N commands given in N
# lines.
# The commands will be pop, remove and discard.
# Input format: 
# The first line contains integer n, the number of elements in the set s.
# The second line contains n space separated elements of set s. All of the elements 
# are non-negative integers, less than or equal to 9.
# Output format:
# Print the sum of the elements of set s on a single line.
# Constraints: 
# 0<n<20
# Input: 
# 5
# 11 23 12 12 25
# 3
# remove 11
# pop
# discard 25
# Output: 
# 35
# Explanation: 
# After completing these 10 operations on the set, we get set([4]). Hence, the sum is 
# 4.
# Note:
# Convert the elements of set s to integers while you are assigning them. To ensure 
# the proper input of the set, we have added the first two lines of code to the editor

# # Given input values
# n = 5
# s = {11, 23, 12, 12, 25}
# N = 3
# commands = ["remove 11", "pop", "discard 25"]

# # Process each command
# for command in commands:
#     operation, *args = command.split()

#     if operation == "remove":
#         element = int(args[0])
#         s.remove(element)
#         print(element)
#     elif operation == "discard":
#         element = int(args[0])
#         s.discard(element)
#         print(element)
#     elif operation == "pop":
#         s.pop()
#         print(element)

# # Print the sum of elements in the set
# print(sum(s))







N = 7
s = {2,5,7,8,4,3,6}
commands = ["remove  7 ", "pop ", "discard 4"]
# commands = input("enter the comamnd Remove , pop , Discard with the value you want to discard: ")

for command in commands:
    operation, *args = command.split()

    if operation == "remove":
        element = int(args[0])
        s.remove(element)
        print(element)

    elif operation == "discard":
        element = int(args[0])
        s.discard(element)
        print(element)

    elif operation =="pop":
        s.pop()


print(sum(s))

# -------------------------------------------------DONE--------------------------------------------------------------------




