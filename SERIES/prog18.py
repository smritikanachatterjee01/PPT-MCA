#18. Find the nth term a,b,b,c,c,c,……………………
import math

def nth_term(n):
    # Find the smallest k such that k(k + 1)/2 >= n
    k = math.ceil((math.sqrt(8 * n + 1) - 1) / 2)
    
    # Map k to the corresponding letter in the alphabet
    # 'a' corresponds to 1, 'b' to 2, ..., 'z' to 26
    letter = chr(ord('a') + k - 1)
    
    return letter

# Example usage:
n = int(input("Enter the value of n: "))
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")