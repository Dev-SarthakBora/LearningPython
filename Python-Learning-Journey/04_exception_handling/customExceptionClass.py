# Q4. Custom Exception – Negative Number

# Create a custom exception class NegativeNumberError.
# Write a program that takes a number as input and raises this exception if the number is negative.
# Catch the exception and print a proper message.

class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

try:
    number = int(input("Enter a number: "))
    if number < 0:
        raise NegativeNumberError("Number is negative") # the object is created here and passed to the Exception class 
                                                        # thus Exception acts as self in a class
    print("Number is:", number)

except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Invalid input! Please enter an integer.")


    


