# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Input
# String
# output
# boolean
# Constraints: 
# • 1 <= s.length <= 2 * 105
# • s consists only of printable ASCII characters.
# Example: 
# Example 1: 
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2: 
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3: 
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome


def is_pelendrome(str):
    cleaned_s = ''.join(char.lower() for char in str if char.isalnum())
    # "".join(char.lower() for char in str if char.isalnum())
    print(cleaned_s)

    return cleaned_s == cleaned_s[::-1]

s1 = "tanishq"
s2 = "wow"
s3 = "racecar"

print(is_pelendrome(s1))
print(is_pelendrome(s2))
print(is_pelendrome(s3))

# ----------------------------------------------------DONE--------------------------------------------------------------