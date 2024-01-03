# There are n bulbs that are initially off. You first turn on all the bulbs, then you turn 
# off every second bulb.
# On the third round, you toggle every third bulb (turning on if it's off or turning off if 
# it's on). For the ith round, you toggle every i bulb. For the nth round, you only 
# toggle the last bulb.
# Return the number of bulbs that are on after n rounds.
# Example 1:
# Input: n = 3
# Output: 1
# Explanation: At first, the three bulbs are [off, off, off].
# After the first round, the three bulbs are [on, on, on].
# After the second round, the three bulbs are [on, off, on].
# After the third round, the three bulbs are [on, off, off]. 
# So you should return 1 because there is only one bulb is on.
# Example 2:
# Input: n = 0
# Output: 0
# Example 3:
# Input: n = 1
# Output: 1
# Constraints: 
# • 0 <= n <= 109
# Example: 
# Input: n = 3
# Output: 1
# Explanation: 
 

# At first, the three bulbs are [off, off, off].
# After the first round, the three bulbs are [on, on, on].
# After the second round, the three bulbs are [on, off, on].
# After the third round, the three bulbs are [on, off, off].
# So you should return 1 because there is only one bulb is on
# def bulbSwitch(n):
#     return int(n**0.5)

# # Example Usage:
# # Example 1:
# n1 = 3
# result1 = bulbSwitch(n1)
# print("Example 1:", result1)  # Output: 1

# # Example 2:
# n2 = 0
# result2 = bulbSwitch(n2)
# print("Example 2:", result2)  # Output: 0

# # Example 3:
# n3 = 1
# result3 = bulbSwitch(n3)
# print("Example 3:", result3)  # Output: 1

def bulbSwitch(n):
    return int(n ** 0.5)

n1 = int(input("enter the no: "))
result1 = bulbSwitch(n1)
print(result1)

n2 = int(input("enter the no: "))
result2 = bulbSwitch(n2)
print(result2)

n3 = int(input("enter the no: "))
result3 = bulbSwitch(n3)
print(result3)

n4 = int(input("enter the no: "))
result4 = bulbSwitch(n4)
print(result4)

# -----------------------------------------------------DONE--------------------------------------------------------------