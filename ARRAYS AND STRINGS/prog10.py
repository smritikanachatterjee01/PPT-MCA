# 10. Program to input a list of numbers and sort using insertion sort:

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Input a list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Perform insertion sort
insertion_sort(numbers)

# Print the sorted list
print("Sorted list using insertion sort:", numbers)