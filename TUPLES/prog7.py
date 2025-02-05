# 7. Tuple Membership Test
def check_membership(t, element):
  return element in t

my_tuple = (10, 20, 30)
print("20 is in the tuple:", check_membership(my_tuple, 20))
print("40 is in the tuple:", check_membership(my_tuple, 40))


