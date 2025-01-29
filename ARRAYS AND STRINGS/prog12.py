# 12. Program to find the frequency of characters in a given string:

def character_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Input a string
string = input("Enter a string: ")

# Find character frequencies
freq = character_frequency(string)

# Print the result
print("Character frequencies:")
for char, count in freq.items():
    print(f"'{char}': {count}")