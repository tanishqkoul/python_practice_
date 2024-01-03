def replace_first_occurrence(s1, s2, s3):
    index = s1.lower().find(s2.lower())
    if index != -1:
        modified_string = s1[:index] + s3 + s1[index + len(s2):]
        return modified_string
    else:
        return s1

s1 = "Hi Tanishq how are you! I am doing great you tell how are you"
s2 = "hi"
s3 = "East or west "
modified_string = replace_first_occurrence(s1, s2, s3)
print("Original string : ",s1)
print("Modified string : ",modified_string)

# ------------------------------------------DONE-----------------------------------------------------------------------
