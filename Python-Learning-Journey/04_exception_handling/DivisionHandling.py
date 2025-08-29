# Handle ZeroDivisionError if the denominator is zero.
# Handle ValueError if the input is not an integer.

def DivisionCheck(numerator:int,denominator:int):
    try:
        result =  int(numerator)/int(denominator)
    except ZeroDivisionError :
        print("Division By zero is not valid")
    except ValueError :
        print("The numbers should be of type int or float")    
    else:    
        print("Division done successfully")   
        return result
    
numerator =  input("Enter the numerator")
denominator=  input("Enter the denominator")

print(DivisionCheck(numerator=numerator,denominator=denominator))    