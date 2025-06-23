username = input("Please enter your username: ")

email = input("Please enter your email: ")

valid_user = username or "User"

print(f"Hello {valid_user}, " + ((email and f"you email is {email}") or ("please provide your email")))