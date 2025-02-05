# 3. Checking Key Existence
def check_key(d, key):
    return key in d

my_dict = {"a": 1, "b": 2, "c": 3}

print("Is 'b' a key in my_dict?", check_key(my_dict, "b"))
print("Is 'd' a key in my_dict?", check_key(my_dict, "d"))