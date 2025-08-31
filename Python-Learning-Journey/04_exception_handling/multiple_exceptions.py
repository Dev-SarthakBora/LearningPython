# multiple_exceptions.py
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print(" Error: Division by zero is not allowed.")
    except TypeError:
        print(" Error: Both values must be numbers (int or float).")
    except Exception as e:  # generic fallback for unexpected errors
        print(f" An unexpected error occurred: {e}")
    else:
        print(" Division successful!")
    finally:
        print(" Operation complete.\n")

# Test cases
divide_numbers(10, 2)      # normal case
divide_numbers(10, 0)      # ZeroDivisionError
divide_numbers(10, "abc")  # TypeError
divide_numbers(None, 5)    # generic exception

