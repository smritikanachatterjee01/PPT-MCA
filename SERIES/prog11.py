#11. Find the nth term 3,5,33,35,53,……………………..
from itertools import product

def generate_sequence(n):
    sequence = []
    length = 1
    while len(sequence) < n:
        # Generate all numbers of the current length using digits 3 and 5
        for num_tuple in product('35', repeat=length):
            num = int(''.join(num_tuple))
            sequence.append(num)
        length += 1
    return sequence[:n]

def nth_term(n):
    sequence = generate_sequence(n)
    return sequence[-1]  # Return the nth term

# Example usage:
n = int(input("Enter the value of n: "))
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")