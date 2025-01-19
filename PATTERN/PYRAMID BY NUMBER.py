# Initialize the starting number
num = 200

# Number of rows
rows = 1000

# Loop through each row
for i in range(1, rows + 1):
    # Loop through each number in the row
    for j in range(i):
        # Print the number and increment it
        print(num, end=" ")
        num += 1
    # Move to the next line after each row
    print()