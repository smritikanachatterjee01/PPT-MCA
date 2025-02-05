# 8. Converting a Tuple to a List & Vice Versa
my_tuple = (10, 20, 30, 40, 50)

my_list = list(my_tuple)  # Converting to a list
print("List:", my_list)

my_list[1] = 25  # Modifying the list
print("Modified list:", my_list)

my_tuple = tuple(my_list)  # Converting back to a tuple
print("Tuple:", my_tuple)