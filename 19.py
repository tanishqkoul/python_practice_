# Honey is given with a collection of n strings in which some strings are of a repeating nature but he has been given with
#  a number k. His task is to find the kth unique string. Also before finding the kth unique string he has to 
# sort each individual string beforehand. If there are fewer unique strings than k print -1.
# As his best friend, your task is to help Ashish in accomplishing the task.
# Input Format 
# • The first line contains an integer n denoting the number of strings.
# • The next n lines contain strings.
# • The next line contains an integer k.
# Output Format 
# The output contains the kth distinct string.
# Constraints: 
# • 1<=n<=105
# • -100<=arr[i]<=100
# Example: 
# Input:
# 6
# d
# b
# c
# b
# c
# a
# 2
# Output:
# a
# Explanation: 
# The only strings in arr that are distinct are "d" and "a." The letter "d" comes first, making it the first 
# separate string. Because "a" appears second, it is the second distinct string. "a" is returned since 
# k == 2

def k_unique_string(Strings, k):
    seen = set()
    unique_string = []
    for s in Strings:
        if s not in seen:
            seen.add(s)
            unique_string.append(s)

    sorted_unique_string = sorted(unique_string)
    print("Unique Sorted string :",sorted_unique_string)#return list
    print(''.join(sorted_unique_string))# return string
    if k <= len(sorted_unique_string):
        return sorted_unique_string[k-1]
    else:
        return -1
n = 6 
Strings = ["d","b","c","b","c","a"]
k = 3 
result = k_unique_string(Strings, k)
print(result)

# --------------------------------------------DONE--------------------------------------------------------------------


