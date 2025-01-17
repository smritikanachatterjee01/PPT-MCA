#3. 1/1^1+2/2^2+3/3^3+………………….+n/n^n
def sum_of_series(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i / (i ** i)
    return total_sum

# Example usage:
n = int(input("Enter a number: "))
result = sum_of_series(n)
print(f"The sum of the series 1/1^1 + 2/2^2 + ... + {n}/{n}^{n} is: {result}")