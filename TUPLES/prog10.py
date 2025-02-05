#  10. Nested Tuples & Accessing Elements
nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))

# Print the second element of the second inner tuple.
print("\nSecond element of the second inner tuple:", nested_tuple[1][1])

# Extract the last element of the third inner tuple.
print("Last element of the third inner tuple:", nested_tuple[2][-1]) # or nested_tuple[2][1]