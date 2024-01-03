# Create an Empty List ‘L’,and move all zero digits to the end (or Right side)of a given list of 
# numbers.Print empty list if list size is zero, Otherwise Print list after segregation.
# Input Format : 
# First line , List size
# Next lines , List Elements
# Output Format : 
# Print list after segregation
# Constraints: 
# List size > 0

def non_zeros_list(L):
    non_zeros = [num for num in L if  num != 0 ]
    zeros = [num for num in L if  num == 0]
    segrated_list = non_zeros + zeros
    return segrated_list

def main():
    size = 14 
    L = [1,0,34,0,45,0,33,0,0,22,567,7,8,8]
    print("original list :", L)
    segregated_list = non_zeros_list(L)
    print("Segregated list:", segregated_list)


if __name__ == "__main__":
    main()
# --------------------------------------------MAIN-------------------------------------------------------------------------