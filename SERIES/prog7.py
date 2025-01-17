#7. 1-1/2+1/3-1/4+………………………………………………..
def sum_of_series(n):
    total_sum = 0
    for i in range(1, n + 1):
        term = ((-1) ** (i + 1)) / i  # Calculate the i-th term
        total_sum += term
    return total_sum

# Example usage:
n = int(input("Enter the number of terms (n): "))
result = sum_of_series(n)
print(f"The sum of the series up to {n} terms is: {result}")