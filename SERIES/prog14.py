#14. Find the nth term 1,1,2,6,24,………………………………
import math

def nth_term(n):
    return math.factorial(n - 1)  # Since the sequence starts from n=1

# Example usage:
n = int(input("Enter the value of n: "))
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")