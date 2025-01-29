# 15. Find the position of the first occurrence of the word 'because' in the sentence:

sentence = "You cannot end a sentence with because because because is a conjunction"
word = "because"

# Find the position of the first occurrence of the word
position = sentence.find(word)

# Print the result
print(f"The first occurrence of '{word}' starts at index: {position}")