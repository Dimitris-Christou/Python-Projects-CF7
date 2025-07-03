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
    
    return plus, minus, mul, div

def main():
    lists_of_ints = [26, 5, 4, 3, 2, 1]

    plus_func, minus_func, mull_func, div_func = calculate(lists_of_ints)

    print(f"Plus func: {plus_func()}")
    print(f"Minus func: {minus_func()}")
    print(f"Mull func: {mull_func()}")
    print(f"Div func: {div_func()}")

if __name__ == "__main__":
    main()