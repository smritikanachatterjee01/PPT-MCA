#15. Find the nth term 1,8,54,384,…………………………..
import math

def nth_term(n):
    return math.factorial(n) * (n ** 2)

# Example usage:
n = int(input("Enter the value of n: "))
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")