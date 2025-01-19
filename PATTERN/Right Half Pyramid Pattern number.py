#Right Half Pyramid Pattern number

rows = 5

# Loop through each row
for i in range(1, rows + 1):
    # Print numbers from 1 to i for each row
    for j in range(1, i + 1):
        print(j, end=" ")
    # Move to the next line after each row
    print()