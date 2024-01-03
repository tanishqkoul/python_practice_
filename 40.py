# def sum_of_diagonals(matrix):
#     n = len(matrix)
#     diagonal1 = sum(matrix[i][i] for i in range(n))
#     diagonal2 = sum(matrix[i][n - i - 1] for i in range(n))
#     return diagonal1 + diagonal2

# # Example usage:
# matrix = [
#     [3, 6, 9],
#     [5, 10, 15],
#     [4, 8, 12]
# ]

# result = sum_of_diagonals(matrix)
# print("Output:", result)


def sum_of_diagonals(matrix):
    n = len(matrix)
    diagonal1 = sum(matrix[i][i] for i in range(n))
    diagonal2 = sum(matrix[i][n - i - 1] for i in range(n))
    return diagonal1 + diagonal2 

matrix = [
    [3 , 6 ,9],
    [2 , 6, 2],
    [1 , 5, 8]
]
result = sum_of_diagonals(matrix)
print(result)

# ---------------------------------------------------DONE----------------------------------------------------------------------