# 11. Program to input a list of numbers and sort using selection sort:

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Input a list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Perform selection sort
selection_sort(numbers)

# Print the sorted list
print("Sorted list using selection sort:", numbers)
