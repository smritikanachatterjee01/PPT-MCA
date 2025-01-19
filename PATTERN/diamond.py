# Number of rows for the upper half of the diamond
rows = 4

# Upper half of the diamond
for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Print '*' with spaces in between
    for k in range(i):
        print("*", end=" ")
    
    # Move to the next line
    print()

# Lower half of the diamond
for i in range(rows - 1, 0, -1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Print '*' with spaces in between
    for k in range(i):
        print("*", end=" ")
    
    # Move to the next line
    print()