# Number of rows
rows = 4

# Loop through each row
for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Print '*' (2*i - 1) times
    for k in range(2 * i - 1):
        print("*", end="")
    
    # Move to the next line
    print()