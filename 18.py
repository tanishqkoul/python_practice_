# A permutation is simply a re-arrangement of the elements in different possible orders. Strings are 
# made up of characters. Permutation of a string will be the set of all possible ways in which the 
# order of the characters of the string can be changed. Print different permutations of a given string
# Input:
# Line 1: input string
# Output:
# Line 1:strings with different possibilities in new lines
# Constraints: 
# 0 <= s.length <= 500000
# String contains unique elements.
# Example: 
# Input : str = 'ABC'
# Output : ABC
#          ACB
#          BAC
#          BCA
#          CAB
#          CBA
# Explanation: 
from itertools import permutations

def print_permutations(input_str):
    all_permutations = permutations(input_str)
    for prem in all_permutations:
        print(''.join(prem))

input_str = "Tanishq"
print_permutations(input_str)

# -----------------------------------------------DONE------------------------------------------------------------------------