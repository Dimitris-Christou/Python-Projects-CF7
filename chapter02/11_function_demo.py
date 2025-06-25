def say_hello(name: str = "there!"):
    """
    Print a greeting message.

    Args:
        name (str): The name to greet. Default value 'there!'
    """
    print(f"Hello {name}")

def main():
    # say_hello(10)
    say_hello()
    say_hello("General Kenobi!")
    
    # print(say_hello.__doc__)
    help(say_hello)
    pass
    

# this condition is true inside this module
if __name__ == "__main__":  
    main()