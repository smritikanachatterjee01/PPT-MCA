#6. Program to rearrange a sorted array alternatively (max, min, second max, second min, etc.):

def rearrange_alternatively(arr, n):
    # Initialize two pointers
    left = 0
    right = n - 1
    result = []

    # Traverse the array and rearrange
    for i in range(n):
        if i % 2 == 0:
            result.append(arr[right])
            right -= 1
        else:
            result.append(arr[left])
            left += 1

    return result

# Example usage
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
rearranged_array = rearrange_alternatively(arr, n)
print("Rearranged array:", rearranged_array)