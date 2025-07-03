def department_id_generator(department):
    last_id = 0

    def generate_id():
        nonlocal last_id
        last_id += 1
        return f"{department}-{last_id}", last_id
    
    return generate_id

def main():
    python_id_generator = department_id_generator("Python")
    
    android_id_generator = department_id_generator("Android")

    print(f"python_id_generator: {type(python_id_generator)}")
   
    print(python_id_generator())    #('Python-1', 1)
    print(python_id_generator())    #('Python-2', 2)

    print(android_id_generator())   #('Android-1', 1)
    print(android_id_generator())   #('Android-2', 2)

if __name__ == "__main__":
    main()