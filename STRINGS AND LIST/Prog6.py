# 6. Check if Two Strings Are Anagrams
from collections import Counter

def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

# Example usage
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False

s3 = "hello"
s4 = "world"
print(f"Are '{s3}' and '{s4}' anagrams? {is_anagram(s3, s4)}")
