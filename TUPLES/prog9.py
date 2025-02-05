# 9. Returning Multiple Values from a Function using Tuples
def math_operations(a, b):
  sum_result = a + b
  difference_result = a - b
  product_result = a * b
  if b != 0:  # To avoid division by zero
    quotient_result = a / b
  else:
    quotient_result = "Undefined (division by zero)"
  return (sum_result, difference_result, product_result, quotient_result)

result = math_operations(10, 5)
print("Results:", result)
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Quotient:", result[3])

result2 = math_operations(10, 0) # Example with division by zero
print("\nResults for 10 and 0:", result2)


