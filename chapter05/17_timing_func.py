import time

def get_time(num):
    start_time = time.time()
    # a few moments later...
    result = sum(range(num))
    end_time = time.time()

    print(f"Functon took {end_time - start_time} seconds to run!")
    return result


def main():
    print(get_time(1000000))

if __name__ == "__main__":
    main()