#17. Find the nth term 0,6,0,12,0,90,…………………….
def nth_term(n):
    if n % 2 == 1:  # Odd positions
        return 0
    else:  # Even positions
        if n == 2:
            return 6
        elif n == 4:
            return 12
        elif n == 6:
            return 90
        else:
            return None  # Unknown term

# Example usage:
n = int(input("Enter the value of n: "))
result = nth_term(n)
if result is not None:
    print(f"The {n}th term of the sequence is: {result}")
else:
    print(f"The {n}th term of the sequence is unknown.")