#16. Find the nth term 5,13,25,41,61,…………………….
def nth_term(n):
    return 2 * n**2 + 2 * n + 1

# Example usage:
n = int(input("Enter the value of n: "))
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")