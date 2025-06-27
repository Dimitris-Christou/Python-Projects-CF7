def compare_intergers(a, b):
    if a == b:
        print("The numbers are equal.")
    elif a > b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{a} is smaller than {b}")

def main():
    try:
        a = int(input("Please enter the first number: "))
        b = int(input("Please enter the second number: "))
    except ValueError:
        print("Invalid input.")
        return
    
    compare_intergers(a, b)

    # 1. simple example ternary operator
    
    # if a > 0:
    #     print("positive")
    # else:
    #     print("non-positive")

    print("positive" if a > 0 else "non-positive")

    # 2. extended example (ternary operator)

    print(f"{a} is equal to {b}" if a == b else
          f"{a} is greater than {b}" if a > b else
          f"{a} is smaller than {b}"
          )
    

if __name__ == "__main__":
    main()