#2. 1/1!+2/2!+3/3!+…………+n/n!
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_series(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i / factorial(i)
    return total_sum

# Example usage:
n = int(input("Enter a number: "))
result = sum_of_series(n)
print(f"The sum of the series 1/1! + 2/2! + ... + {n}/{n}! is: {result}")