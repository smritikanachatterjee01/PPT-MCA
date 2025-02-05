# 3. Immutable Nature of Tuples
my_tuple = (4, 8, 12, 16)

# Trying to modify the second element (this will cause an error)
try:
  my_tuple[1] = 10 
except TypeError as e:
  print("Error:", e)

print("Original tuple (unchanged):", my_tuple)