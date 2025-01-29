# 9. Program to input a list of numbers and sort using bubble sort:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Input a list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Perform bubble sort
bubble_sort(numbers)

# Print the sorted list
print("Sorted list:", numbers)