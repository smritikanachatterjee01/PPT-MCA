# 17. Use string formatting to display the area of a circle:
radius = 10
area = 3.14 * radius**2

# Using f-string (Python 3.6+)
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Using format() method
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

# Using %-formatting
print("The area of a circle with radius %d is %.0f meters square." % (radius, area))