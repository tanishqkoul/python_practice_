file_path = "nonexistent_file.txt"
with open(file_path, 'r') as file:
    content = file.read()
    file.close()
print(content)

# file_path = "nonexistent_file.txt"

# try:
#     with open(file_path, 'r') as file:
#         content = file.read()
#     print(content)
# except FileNotFoundError:
#     print(f"Error: File '{file_path}' not found.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
