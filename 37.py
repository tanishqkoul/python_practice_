# Write a Code to Read and print given string's even indexed character in
# Uppercase and remaining it should be same.
# Input: 
# JhansiRani
# Output: 
# JhAnSiRaNi
# def process_string(input_str):
#     result = ""

#     for i in range(len(input_str)):
#         if i % 2 == 0:
#             result += input_str[i].upper()
#         else:
#             result += input_str[i]

#     return result

# # Example usage:
# input_string = "JhansiRani"
# result = process_string(input_string)
# print("Output:", result)
def Process_string(input_str):
    result = ""

    for i in range(len(input_str)):
        print(len(input_str))
        if i % 2 == 0 :
            result += input_str[i].upper()
        else:
            result += input_str[i]

    return result   

input_str = "jhasikirani"
result = Process_string(input_str)
print(result)

# ================================================DONE=================================================================