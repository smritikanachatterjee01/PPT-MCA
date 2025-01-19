# Number of rows
rows = 5

# Loop through each row
for i in range(1, rows + 1):
    # Print leading spaces for alignment
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Print stars
    for k in range(i):
        print("*", end=" ")
    
    # Move to the next line after each row
    print()