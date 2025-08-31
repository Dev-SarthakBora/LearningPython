# Q3. File Reader with Finally

# Write a program that:

# Asks the user for a filename.

# Tries to open and read the file.

# Handles FileNotFoundError if the file does not exist.

# Uses a finally block to print "Program ended" no matter what happens.
import os

filename = input("Enter the filename: ")
path = os.path.abspath(filename)
print(path)

try:
    with open(path, 'r') as file:   
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("The file you are looking for is not here")
finally:
    print("Program Ended")
