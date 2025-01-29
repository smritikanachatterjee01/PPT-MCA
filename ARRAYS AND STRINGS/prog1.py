#1. Program to input a 4-digit number and print even and odd digits, and total even and odd digits:

# Input a 4-digit number
number = input("Enter a 4-digit number: ")

# Initialize counters
even_digits = []
odd_digits = []

# Iterate through each digit
for digit in number:
    if int(digit) % 2 == 0:
        even_digits.append(digit)
    else:
        odd_digits.append(digit)

# Print results
print("Even digits:", ", ".join(even_digits))
print("Odd digits:", ", ".join(odd_digits))
print("Total even digits:", len(even_digits))
print("Total odd digits:", len(odd_digits))