# 1. Removing All Duplicates from a String
def remove_duplicates(s):
    return "".join(dict.fromkeys(s))

s = "programming"
print(remove_duplicates(s))  
