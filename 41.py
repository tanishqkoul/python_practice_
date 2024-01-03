# def print_substrings(input_str):
#     n = len(input_str)

#     for i in range(n):
#         for j in range(i, n):
#             print(input_str[i:j+1])

# # Example usage:
# input_string = "ABCD"
# print_substrings(input_string)

def print_substrings(input_str):
    n = len(input_str)

    for i in range(n):
        for j in range(i, n):
            print(input_str[i:j+1])

input_str = "TANI"
result = print_substrings(input_str)
print(result)

# ------------------------------------------DONE----------------------------------------------------------------------------