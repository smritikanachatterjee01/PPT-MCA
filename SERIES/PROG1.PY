#1. 1!+2!+3!+…………….+n! 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_factorials(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += factorial(i)
    return total_sum

# Example usage:
n = int(input("Enter a number: "))
result = sum_of_factorials(n)
print(f"The sum of factorials from 1! to {n}! is: {result}")