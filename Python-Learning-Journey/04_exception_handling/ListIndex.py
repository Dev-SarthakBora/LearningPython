def ListIndex(numbers: list):
    try:
        index = int(input("Enter the index :: "))
        element = numbers[index]
    except ValueError:
        print("The Entered value is not an integer")
    except IndexError:
        print("List index out of range")
    else:
        return element    


numbers = []
try:
    size = int(input("Enter the size of the list: "))
    for i in range(size):
        element = int(input("Enter element {}: ".format(i)))
        numbers.append(element)
except ValueError:
    print("Please enter only integers for size and elements.")

result = ListIndex(numbers)
if result is not None:
    print("Element at index is:", result)
