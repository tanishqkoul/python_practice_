# You have n super washing machines on a line. Initially, each washing machine has 
# some dresses or is empty.
# For each move, you could choose any m (1 <= m <= n) washing machines, and 
# pass one dress of each washing machine to one of its adjacent washing machines 
# at the same time.
# Given an integer array machines representing the number of dresses in each 
# washing machine from left to right on the line, return the minimum number of
# moves to make all the washing machines have the same number of dresses. If it is 
# not possible to do it, return -1.
 

# Example 1:
# Input: machines = [1,0,5]
# Output: 3
# Explanation:
# 1st move: 1 0 <-- 5 => 1 1 4
# 2nd move: 1 <-- 1 <-- 4 => 2 1 3
# 3rd move: 2 1 <-- 3 => 2 2 2
# Example 2:
# Input: machines = [0,3,0]
# Output: 2
# Explanation:
# 1st move: 0 <-- 3 0 => 1 2 0
# 2nd move: 1 2 --> 0 => 1 1 1
# Example 3:
# Input: machines = [0,2,0]
# Output: -1
# Explanation:
# It's impossible to make all three washing machines have the same number of 
# dresses.
# Constraints: 
# • n == machines.length
# • 1 <= n <= 104
# • 0 <= machines[i] <= 105
# Example: 
# Example 1:
# Input: machines = [1,0,5]
# Output: 3
# Explanation: 
# 1st move: 1 0 <-- 5 => 1 1 4
# 2nd move: 1 <-- 1 <-- 4 => 2 1 3
# 3rd move: 2 1 <-- 3 => 2 2 2

def find_min_moves(machines):
    total_dresses = sum(machines)
    n = len(machines)

    if total_dresses % n != 0:
        return -1  # If the total dresses cannot be equally distributed, return -1

    target_dresses = total_dresses // n
    moves, balance = 0, 0

    for dresses in machines:
        imbalance = dresses - target_dresses
        balance += imbalance
        moves = max(moves, abs(balance), imbalance)

    return moves

# Example usage:
machines1 = [1, 0, 5]
machines2 = [0, 3, 0]
machines3 = [0, 2, 0]

result1 = find_min_moves(machines1)
result2 = find_min_moves(machines2)
result3 = find_min_moves(machines3)

print("Example 1:", result1)
print("Example 2:", result2)
print("Example 3:", result3)
