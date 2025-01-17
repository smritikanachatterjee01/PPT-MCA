#10. Find the nth term 2,4,3,4,15,…………………………
def nth_term(n):
    if n % 2 == 0:  # Even positions
        return 4
    else:  # Odd positions
        if n == 1:
            return 2
        elif n == 3:
            return 3
        elif n == 5:
            return 15
        else:
            return None  # Unknown term

# Example usage:
n = int(input("Enter the value of n: "))
result = nth_term(n)
if result is not None:
    print(f"The {n}th term of the sequence is: {result}")
else:
    print(f"The {n}th term of the sequence is unknown.")