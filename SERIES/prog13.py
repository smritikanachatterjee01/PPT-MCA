#13. Find the nth term 14,28,20,40,…………………………….
def nth_term(n):
    if n == 1:
        return 14
    elif n % 2 == 0:
        return 2 * nth_term(n - 1)
    else:
        return nth_term(n - 1) - 8

# Example usage:
n = int(input("Enter the value of n: "))
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")