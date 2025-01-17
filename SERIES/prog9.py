#9. 1+2+11+26+47+……………………………………………..
def sum_of_series(n):
    total_sum = 0
    for k in range(1, n + 1):
        term = 4 * k**2 - 11 * k + 8  # Calculate the k-th term
        total_sum += term
    return total_sum

# Example usage:
n = int(input("Enter the number of terms (n): "))
result = sum_of_series(n)
print(f"The sum of the series up to {n} terms is: {result}")