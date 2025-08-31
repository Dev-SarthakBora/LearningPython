# operators.py

# Arithmetic Operators
a, b = 10, 3
print("Arithmetic Operators:")
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division
print("a // b =", a // b) # Floor Division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponentiation
print()

# Comparison Operators
print("Comparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print()

# Logical Operators
x, y = True, False
print("Logical Operators:")
print("x and y =", x and y)
print("x or y  =", x or y)
print("not x   =", not x)
print()

# Assignment Operators
print("Assignment Operators:")
c = 5
print("c =", c)
c += 2  # c = c + 2
print("c += 2:", c)
c -= 1
print("c -= 1:", c)
c *= 3
print("c *= 3:", c)
c //= 2
print("c //= 2:", c)
c %= 4
print("c %= 4:", c)
c **= 2
print("c **= 2:", c)
print()

# Bitwise Operators
m, n = 6, 3   # binary: m=110, n=011
print("Bitwise Operators:")
print("m & n =", m & n)   # AND
print("m | n =", m | n)   # OR
print("m ^ n =", m ^ n)   # XOR
print("~m =", ~m)         # NOT
print("m << 1 =", m << 1) # Left shift
print("m >> 1 =", m >> 1) # Right shift
print()

# Membership Operators
list1 = [1, 2, 3, 4, 5]
print("Membership Operators:")
print("3 in list1:", 3 in list1)
print("10 not in list1:", 10 not in list1)
print()

# Identity Operators
p, q = [1, 2], [1, 2]
r = p
print("Identity Operators:")
print("p is r:", p is r)          # Same object
print("p is q:", p is q)          # Different objects
print("p == q:", p == q)          # Same values
