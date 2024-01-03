my_dict = {'a': 1, 'b': 2, 'c': 3, "d": 100}
value = input("Enter the key to be searched: ")

# Check if the key is present in the dictionary
if value in my_dict:
    print(f"The value of {value}: {my_dict[value]}")
else:
    print(f"The key {value} is not present in the dictionary.")
