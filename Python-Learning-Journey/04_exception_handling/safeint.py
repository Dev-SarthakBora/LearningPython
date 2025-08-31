# 🔹 Q5. Exception Chaining

# Write a function safe_int(value) that:

# Tries to convert a string value to an integer.

# If conversion fails, catch the ValueError and raise a new exception TypeError("Conversion failed") using raise ... from ....

# Demonstrate calling this function with both valid and invalid inputs.
def safe_int(value):
    try:
        try:
            intvalue = int(value)
            print(intvalue, type(intvalue))
        except ValueError:
            raise TypeError("the program ended")
    except TypeError:
        print("conversion failed")




safe_int(5)
safe_int("hhgjh")
