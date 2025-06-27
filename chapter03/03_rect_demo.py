# Create a function that checks if a rectangular is a square.

def is_square(length: int, width: int) -> bool:
    """
    Checks if a rectangular is a square.

    Args:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle

    Returns: 
        bool: True if rectangle is square, False otherwise.
     
    """
    return length == width

def main():
    try:
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))

        if is_square(length,width):
            print("The rectangle is a square.")
        else:
            print("The rectangle is not a square.")
        
    except ValueError:
        print("Invalid input. Please enter int.")
        # return

if __name__ == "__main__":
    main()