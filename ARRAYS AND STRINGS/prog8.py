# 8. Program to input a number and search in a list using binary search:

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Return -1 if target is not found

# Input list (must be sorted) and target number
arr = [10, 20, 30, 40, 50]
target = int(input("Enter the number to search: "))

# Perform binary search
result = binary_search(arr, target)

# Print the result
if result != -1:
    print(f"Number found at index {result}.")
else:
    print("Number not found in the list.")