# 1.	Interchange First and Last Elements in a List
def interchange_first_last(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

lst = [1, 2, 3, 4, 5]
print(interchange_first_last(lst))  
