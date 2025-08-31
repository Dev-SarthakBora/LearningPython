# input_output.py
# Taking input as string
name = input("Enter your name: ")
print("Hello,", name)

# Taking integer input
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Taking float input
height = float(input("Enter your height in meters: "))
print("Your height is:", height, "meters.")

# Taking multiple inputs in one line
x, y = input("Enter two numbers separated by space: ").split()
print("You entered:", x, "and", y)

# Converting multiple inputs to integers
a, b = map(int, input("Enter two integers separated by space: ").split())
print("Sum =", a + b)

# Output formatting (f-string)
print(f"{name}, you are {age} years old and {height:.2f} meters tall.")

