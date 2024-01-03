def divide_numbers(a, b):
    if b==0:
        raise ValueError("Division by zero is not allowed")
    else:
        result = a/b
        return result

a =  int(input("enter the 1 no you want to divide : "))
b =  int(input("enter the 2 no you want to divide : "))
result = divide_numbers(a,b)
print(result)