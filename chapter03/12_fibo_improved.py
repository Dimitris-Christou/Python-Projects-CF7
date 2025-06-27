def fibonacci(n):
    if n in (0, 1): return n

    a, b = 0, 1
    
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

def main():
    pass

if __name__ == "__main__":
    main()