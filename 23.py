# # Write a program to print n non composite numbers after nth Prime number

def is_prime(n):
    if n<2:
        return False
    return all(n % i != 0 for i in range(2,int(n **0.5)+ 1 ))

def nth_prime_no(n):
    prime_count = 0
    num = 2
    while (prime_count<n):
        if is_prime(num):
            prime_count += 1 
        num += 1
    return num - 1 

def non_composite_after_nth_prime( n,count):
    nth_prime = nth_prime_no(n)
    non_composite_count = 0
    num = nth_prime + 1

    while non_composite_count < count:
        if not is_prime(num):
            non_composite_count += 1
            print(num)
        num += 1

n = 3
count = 5
non_composite_after_nth_prime(n, count)


