# You are given a list N integers,and an integer M.Print all the elements of the list as square of 
# elements are divisible of M and cube of elements which are not divisible by M.

# Input format : 
# Line 1 , List size 

# Line 2 , List elements
# Line 3 , Integer 'M'
# Output format : 
# Print output
# Constraints: 
# NA
# Example: 
# Input :
# size = 5
# list=1 2 3 4 5
# M=3
# Output:
# 1 8 9 64 125

def calculations(elements,M):
    result = []
    for i in elements:
        if i % M == 0:
            result.append(i**2)
        else :
            result.append(i**3)
    return result


def main():
    n = 5
    elements = [3,4,9,5,2,1]
    M = 3
    result = calculations(elements,M)
    print(result)
    print(" ".join(map(str, result))) #return string 

if __name__ == "__main__":
    main()
    #  ------------------------------------------------DONE-------------------------------------------------------------------