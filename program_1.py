# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):
    """
    Converts kilometers to miles and returns the result.
    """
    miles = kilometers * 0.6214
    return miles


if __name__ == '__main__':
    # Get User Input
    km = float(input("Enter a distance in kilometers: "))

    # Call kilometer_conversion
    miles = kilometer_conversion(km)

    # Display the miles
    print(f"{km} kilometers is equal to {miles:.2f} miles.")

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    
    # Display the miles
