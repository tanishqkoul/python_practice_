# 1.Description:(You can apply oops concept here try) 
# 1) the function search() which takes the string S and the string bat as inputs and returns an
# array denoting the start indices (1-based)  Print the indexes of all the occurrences of pattern
# string in the text string. 
# 2) the function search() which takes the string S and the string pat as inputs and returns an
# array denoting the start indices (1-based) of substring pat in the string S. 
# Constraints: 
# Example: 
# Explanation: 
# The sub String bat id occurred at f character position 1 and 18th

# class StringSearch:
#     def __init__(self, text):
#         self.text = text

#     def search(self, pattern):
#         indices = []
#         index = self.text.find(pattern) + 1

#         while index:
#             indices.append(index)
#             index = self.text.find(pattern, index) + 1

#         return indices

# # Example Usage:
# text_string = "The sub String bat is occurred at f character position 1 and 18th"
# search_instance = StringSearch(text_string)

# # Search for the pattern "bat"
# pattern = "bat"
# result_indices = search_instance.search(pattern)

# if result_indices:
#     print(f"The pattern '{pattern}' is found at positions: {result_indices}")
# else:
#     print(f"The pattern '{pattern}' is not found in the text.")

class StringSearch:
    def __init__(self, text):
        self.text = text

    def search(self, pattern):
        indices = []
        Index = self.text.find(pattern) + 1
     
        while Index:
            indices.append(Index)
            Index = self.text.find(pattern, Index) + 1
        return indices
    
text_string = input("Enter the string : ")
search_instance =  StringSearch(text_string)

pattern = "bat"
result_indices = search_instance.search(pattern)

if result_indices:
    print(f"The {pattern} is found at position : {result_indices} ")
else:
    print(f"the {pattern}is not found in the text")

# -----------------------------------------------------DONE----------------------------------------------------------------------- 