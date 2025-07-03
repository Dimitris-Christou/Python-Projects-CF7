import functools
# from functools import reduce

def calculate(args):
    def plus():
        return functools.reduce(lambda x,y: x + y, args)

    def minus():
        return functools.reduce(lambda x,y: x - y, args)
    
    def mul():
        return functools.reduce(lambda x,y: x * y, args)

    def div():
        # if not 0 in args[1:0]:...
        return args[0] / sum(args[1:])   
    
    # we return a dictionary instead of tuple
    return {
        "add" : plus, 
        "subtract" : minus,
        "multipy" : mul,
        "division" : div
    }

def main():
    lists_of_ints = [26, 5, 4, 3, 2, 1]

    operations = calculate(lists_of_ints)

    while True:
        print("\nChoose an operaton")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Please enter a number between 1 and 5: "))
        except ValueError:
            print("Invalid input")
            continue

        match choice:
            case 1:
                print("Addition:", operations["add"]())
            case 2:
                print("Subtraction:", operations["subtract"]())
            case 3:
                print("Multiplication:", operations["multipy"]())
            case 4:
                print("Division:", operations["division"]())
            case 5:
                print("Goodbye")
                break
            case _:
                print("Invalid input.Please try again.")

if __name__ == "__main__":
    main()