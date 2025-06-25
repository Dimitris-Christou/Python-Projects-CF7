class student:
    """
    A class that represents a student with a first name and a last name.

    Attrs:
    firstname (str): The first name of the student. Defaults to Jhon.
    lastname (str): The last name of the student. Defaults to Doe.
    """

    def __init__(self, firstname: str = "Jhon", lastname: str = "Doe"):
        self.firstname = firstname
        self.lastname = lastname

def main():
    st1 = student()
    print(f"{st1.firstname} {st1.lastname}")
    st2 = student("Bob", "Dylan")
    print(f"First name: {st2.firstname}")
    print(f"Last name: {st2.lastname}")

if __name__ == "__main__":
    main()