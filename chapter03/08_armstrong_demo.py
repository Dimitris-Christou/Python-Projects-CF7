def is_armstrong(num): # 153
    digits = str(num)
    power = len(digits)
    total = 0

    # '1', "5", '3'
    for digit in digits:
        total += int(digit)  ** power

    return num == total

def main():
    try:
        num = int(input("Please insert an integer: "))
    except ValueError:
        print("Invalid input")
        return
    
    print(f"{num} is an armstrong number" if is_armstrong(num) else f"{num} is not an armstrong number")

if __name__ == "__main__":
    main()