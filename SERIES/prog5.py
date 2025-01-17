#5. 1*3+3*5+………………………………………………….
def sum_of_series(n):
    total_sum = 0
    for i in range(1, n + 1):
        term = (2 * i - 1) * (2 * i + 1)  # Calculate the i-th term
        total_sum += term
    return total_sum

# Example usage:
n = int(input("Enter the number of terms (n): "))
result = sum_of_series(n)
print(f"The sum of the series up to {n} terms is: {result}")