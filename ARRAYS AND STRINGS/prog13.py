# 13. Program to input a string and a number to encode the string by adding the number to every character in the string:

def encode_string(string, num):
    encoded_string = ""
    for char in string:
        # Shift the character by the given number
        encoded_char = chr(ord(char) + num)
        encoded_string += encoded_char
    return encoded_string

# Input a string and a number
string = input("Enter a string: ")
num = int(input("Enter a number to encode the string: "))

# Encode the string
encoded_string = encode_string(string, num)

# Print the encoded string
print("Encoded string:", encoded_string)