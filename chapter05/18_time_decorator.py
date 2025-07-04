import time

def timer_decorator(func):
    """
    Decorator to measure the execution time of a function.

    Params:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function with added timing functionality.
    """
    def inner_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # execution
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        return result

    return inner_func

def sum_function(n):
    return sum(range(n))



# the printed name of the function changes to time_decorator
my_sum_func = timer_decorator(sum_function)
print(my_sum_func(1000000))

# solution with print


# solution with Decorators
@timer_decorator
def average_func(n):
    if n == 0:
        return 0
    total_sum = sum(range(n))
    return total_sum / n

print(average_func(101))


