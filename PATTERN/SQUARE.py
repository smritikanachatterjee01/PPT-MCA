# Number of rows and columns
rows = 4
columns = 4

# Loop through each row
for i in range(rows):
    # Loop through each column
    for j in range(columns):
        # Print '*' for the first and last row, or first and last column
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("  *", end=" ")
        else:
            print("   ", end=" ")
    # Move to the next line
    print()