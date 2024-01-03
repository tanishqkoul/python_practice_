# Below image shows the standard representation of a chessboard.
# This could be imagined as a 2D cartesian plane, with the x axis being represented by the alphabets and y axis by the numbers.

# Given coordinates in the form of string, print if that cell is white or black.

# If the input is wrong print "-1".

# Input Format 
# First line contains a string s.
# Output Format 
# White or Black.
# Constraints: 
# length of S must be 2
# Example: 
# Input: g3
# Output: Black
# Input: a9
# Output: -1
# Explanation: 
# 1.The 'g' column and row '3' is in color 'Black'
# 2.The 'a' column and row '9' is not present so '-1'


while True:
    def get_color_cell_cordinates(cordinates):
        if len(cordinates) != 2:
            return "-1"
        
        column,Row = cordinates[0],cordinates[1]

        white_column = ["a","c","e","g","i","k"]

        if column.isalpha and Row.isdigit:
            column = column.lower()

            if column in white_column:
                if int(Row) % 2 == 0:
                    return "White"
                else:
                    return "Black"
                
            else:
                if int(Row) % 2 == 0 :
                    return "Black"
                else:
                    return "White"
                

        else:
            return "-1"
        
    cordinates = input("Enter the cordintes in the form of a2, g6 , b2 etc : ")
    result = get_color_cell_cordinates(cordinates)
    print(result)


# -----------------------------------------------------DONE-----------------------------------------------------------------------
        