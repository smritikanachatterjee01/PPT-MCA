#8. 1-x^2/2!+x^4/4!+…………………………………………….
import math

def sum_of_series(x, n):
    total_sum = 0
    for k in range(n + 1):
        term = ((-1) ** k) * (x ** (2 * k)) / math.factorial(2 * k)
        total_sum += term
    return total_sum

# Example usage:
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))
result = sum_of_series(x, n)
print(f"The sum of the series up to {n} terms is: {result}")