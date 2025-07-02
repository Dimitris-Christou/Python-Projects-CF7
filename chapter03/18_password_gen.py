import string
import random

# list to string
characters = list(string.ascii_letters + string.digits + "!@#$%^&*")
# print(characters)

def generate_password():
    """
    Generate a random password based on the user_specified Length.  
    """

    try:
        password_length = int(input("Specify the password length: "))

        if password_length <= 0:
            print("Password length must be a positive number.")
            return
    except ValueError:
        print("Invalid input. Please provide a positive integer.")
        return
    
    random.shuffle(characters)

    password = []
    
    for i in range(password_length):
        password.append(random.choice(characters))
    
    # extra shuffle for extra randomness
    random.shuffle(password)

    # list to string
    password = "".join(password)

    print(f"Generated password: {password}")



def main():
    while True:
        option = input("\nDo you want to create a password? ('y' or 'n'): ")

        if option.lower() == 'y':
            generate_password()
        elif option.lower() == 'n':
            print("Goodbye")
            break
        else:
            print("Wrong Input")

if __name__ == "__main__":
    main()