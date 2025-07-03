def calculator(x, y, operation):
    try:
        return operation(x, y)
    except TypeError as e:
        print(f"Error: {e}. Ensure the 'operation' argument is a function which takes 2 ints as args")

def add(x,y):
    return x + y

def multiply(x,y):
    return x * y

def subtract(x,y):
    return x - y

def main():
    print("Addition", calculator(int(input("Enter an int: ")), int(input("Enter an int: ")), add))
    print("Subtraction", calculator(int(input()), int(input()), subtract))
    print("Multiplication", calculator(100, 40, multiply))


if __name__ == "__main__":
    main()