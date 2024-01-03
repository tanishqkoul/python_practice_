# Write a program to convert a given binary number into an equivalent decimal
# number ?
# Constraints: 
# Binary number must be of 8 digits or below. if the length of the binary number
# is greater than 8 it must return Invalid.
# Example: 
# input:
# 10101010
# output:
# 170
# input 1:
# 1010101010
# output 1:
# Invalid
# Explanation: 
# for input1 : the decimal form of binary number 10101010 is 170.
# for input 2: the given binary number has length of 10 digits. So,it's output is "Invalid".
# def binary_to_decimal(binary_number):
#     # Check if the binary number is of valid length
#     if len(binary_number) > 8:
#         return "Invalid"

#     decimal_number = 0
#     binary_number = binary_number[::-1]  # Reverse the binary number for easier calculation

#     # Iterate through each digit of the binary number
#     for i in range(len(binary_number)):
#         # Check if the digit is '1', then add 2^i to the decimal number
#         if binary_number[i] == '1':
#             decimal_number += 2 ** i

#     return decimal_number

# # Example usage:
# user_input = "11101011"
# result = binary_to_decimal(user_input)

# print(result)
while True:
    def Binary_to_decimal(binary_no):
        if len(binary_no) > 8 :
            return "Inavlid Input"
        
        decimal_no = 0 
        binary_no = binary_no[::-1]#reversing for easy calculations

        for i in range(0, len(binary_no)):
            if binary_no[i] == "1":
                decimal_no += 2 ** i

        return decimal_no

    binary_no = input("Enter no for conversion : ")
    result = Binary_to_decimal(binary_no)
    print(result) 
# ------------------------------------------------------DONE -----------------------------------------------------------------------
    