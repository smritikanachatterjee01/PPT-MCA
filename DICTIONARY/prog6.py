# 6. Merging Two Dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Method 1: Using the update() method (values from d2 overwrite d1)
d1.update(d2)  # Modifies d1 directly
print("Merged dictionary (Method 1):", d1)


# Method 2: Creating a new dictionary (values from d2 take precedence)
d3 = d1.copy()  # Create a copy of d1 to avoid modifying it directly
d3.update(d2)  # Update the copy
print("Merged dictionary (Method 2):", d3)

# Method 3: Using dictionary unpacking (values from d2 take precedence, Python 3.5+)
d4 = {**d1, **d2}
print("Merged dictionary (Method 3):", d4)