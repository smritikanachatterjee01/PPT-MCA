# Number of rows
rows = 4

# Loop through each row
for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Print '*' with spaces in between
    for k in range(i):
        print("*", end=" ")
    
    # Move to the next line
    print()