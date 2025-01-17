#12. Find the nth term 0,0,2,1,4,2,6,3,8……………………….
def nth_term(n):
    if n % 2 == 1:  # Odd position
        return n - 1
    else:  # Even position
        return (n // 2) - 1

# Example usage:
n = int(input("Enter the value of n: "))
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")