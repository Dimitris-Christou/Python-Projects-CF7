def test_args_func(pos_arg1, pos_arg2, opt_arg1=None, opt_arg2=None, *args, **kwargs):
    """
    Function to demonstrate the usage of positional, optional, additional positional (*args) and additional keyword
    arguments (**kwargs).

    Parameters: 
        pos_arg1 (Any): The first positional argument.
        pos_arg2: The second positional argument.
        opt_arg1: The first optional argument. Defaults to None.
        opt_arg2: The second optional argument. Default to None.
        *args: Additional positional arguments.
        **kwargs: Additional keyword arguments.
    """
    # Print positional arguments.
    print(f"Pos arg1: {pos_arg1}")
    print(f"Pos arg2: {pos_arg2}")
    
    # Print optional arguments
    print(f"Opt arg1: {opt_arg1}")
    print(f"Opt arg2: {opt_arg2}")

    # Print additional pos args
    if args:
        print("Additional pos args")
        for arg in args:
            print(arg)

    # Print additional keyword args
    if kwargs:
        print("Additional kwargs")
        for key,value in kwargs.items():
            print(f"{key} : {value}")

def main():
    test_args_func("Hello", "CF7")
    test_args_func("Hello", "CF7", 100)     
    test_args_func("Hello", "CF7", 100, 200)     
    print("-"*10)
    test_args_func("Hello", "CF7", opt_arg2=200)
    print("-"*10)
    test_args_func("Hello", "CF7", name="Duncan Mcleod of the clan Mcleod",age="????")
    print("-"*10)
    test_args_func("Hello", "CF7",                      # pos_arg1, pos_arg1
                   100, 200,                            # opt_arg1, opt_arg2
                   300, "Bob",                          # *args
                   name="Dimitris", street="Coding")    # **kwargs


if __name__ == "__main__":
    main()

# def main():
#     pass

# if __name__ == "__main__":
#     main()