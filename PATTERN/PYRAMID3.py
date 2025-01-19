# Print Pascal's Triangle in Python
from math import factorial

# input n
n = 4
for i in range(n):
    # for left spacing
    for j in range(n - i):
        print(end=" ")
    
    for j in range(i + 1):
        # nCr = n! / ((n-r)! * r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    
    # for new line
    print()