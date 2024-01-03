def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
    return True

# Test the function
number_to_test = 17
result = is_prime(number_to_test)

if result:
    print(f"{number_to_test} is a prime number.")
else:
    print(f"{number_to_test} is not a prime number.")
# --------------------------------------------------------MAIN-----------------------------------------------------------------