# variables.py
# Variable assignment
x = 10              # integer
y = 3.14            # float
name = "Sarthak"    # string
is_active = True    # boolean

print("x =", x)
print("y =", y)
print("name =", name)
print("is_active =", is_active)

# Multiple assignment
a, b, c = 1, 2, 3
print("\nMultiple assignment:", a, b, c)

# Same value to multiple variables
p = q = r = 100
print("Same value assigned:", p, q, r)

# Dynamic typing (Python allows changing types)
value = 42
print("\nInitially:", value, type(value))

value = "Now I'm a string"
print("After reassignment:", value, type(value))

# Variable naming rules (valid examples)
age = 21
_age = 22
age2 = 23
AGE = 24

print("\nDifferent variable names:", age, _age, age2, AGE)

# Using variables in expressions
length = 5
width = 3
area = length * width
print(f"\nArea of rectangle = {area}")

# Deleting a variable
temp = "temporary"
print("\nBefore deleting:", temp)
del temp
# print(temp)  # would cause NameError

