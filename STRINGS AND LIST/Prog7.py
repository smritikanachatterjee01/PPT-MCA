# 7. Replace All Characters Except a Given Character
def replace_except(s, char, replacement='*'):
    return ''.join(c if c == char else replacement for c in s)
s = input("Enter a string: ")
char = input("Enter the character to keep: ")
result = replace_except(s, char)
print(f"Result after replacement: {result}")
