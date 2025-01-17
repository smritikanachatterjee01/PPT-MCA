#6. 1*2*3+2*3*4+……………………………….+n*(n+1)*(n+2)
def sum_of_series(n):
    total_sum = 0
    for i in range(1, n + 1):
        term = i * (i + 1) * (i + 2)  # Calculate the i-th term
        total_sum += term
    return total_sum

# Example usage:
n = int(input("Enter the number of terms (n): "))
result = sum_of_series(n)
print(f"The sum of the series up to {n} terms is: {result}")