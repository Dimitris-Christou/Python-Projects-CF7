def my_add(*args: int) -> int:
    return sum(args)

def my_avg(*args: int) -> float:
    return sum(args) / len(args) if args else 0

def main():
    ages = [27, 18, 35, 22, 32]

    print(f"Total ages: {my_add(*ages)}")
    print(f"Average ages: {my_avg(*ages)}")

if __name__ == "__main__":
    main()