# 4. Program to find all numbers between 1000 and 3000 where each digit is even:
# Function to check if all digits of a number are even
def all_digits_even(num):
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True

# Find and print numbers between 1000 and 3000 with all even digits
result = [num for num in range(1000, 3001) if all_digits_even(num)]
print("Numbers with all even digits between 1000 and 3000:", result)