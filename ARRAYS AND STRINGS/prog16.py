# 16. Slice out the phrase 'because because because' in the sentence:

sentence = "You cannot end a sentence with because because because is a conjunction"
phrase = "because because because"

# Find the start and end indices of the phrase
start_index = sentence.find(phrase)
end_index = start_index + len(phrase)

# Slice out the phrase
sliced_sentence = sentence[:start_index] + sentence[end_index:]

# Print the result
print("Sentence after slicing out the phrase:", sliced_sentence)