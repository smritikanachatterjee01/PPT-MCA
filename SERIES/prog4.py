#4. 1+x+x^2+x^3+……………………………………+x^n
def sum_of_series(x, n):
    total_sum = 0
    for i in range(0, n + 1):  # Loop from 0 to n (inclusive)
        total_sum += x ** i
    return total_sum

# Example usage:
x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
result = sum_of_series(x, n)
print(f"The sum of the series 1 + x + x^2 + ... + x^{n} is: {result}")