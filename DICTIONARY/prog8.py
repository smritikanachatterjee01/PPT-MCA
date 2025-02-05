# 8. Converting Two Lists into a Dictionary
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

# Method 1: Using zip and dict constructor
my_dict = dict(zip(keys, values))
print("Dictionary (Method 1):", my_dict)

# Method 2: Using a loop
my_dict2 = {}
for i in range(len(keys)):
  my_dict2[keys[i]] = values[i]
print("Dictionary (Method 2):", my_dict2)

# Method 3: Dictionary Comprehension (more concise)
my_dict3 = {keys[i]: values[i] for i in range(len(keys))}
print("Dictionary (Method 3):", my_dict3)