# 7. Program to input a number and search in a list using linear search:

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Return -1 if target is not found

# Input list and target number
arr = [10, 20, 30, 40, 50]
target = int(input("Enter the number to search: "))

# Perform linear search
result = linear_search(arr, target)

# Print the result
if result != -1:
    print(f"Number found at index {result}.")
else:
    print("Number not found in the list.")