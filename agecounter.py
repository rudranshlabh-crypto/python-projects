def check_age():
    try:
        user_input = input("Enter your age: ")
        age = int(user_input)
        
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")
        
        if age % 2 == 0:
            print(f"The age {age} is Even.")
        else:
            print(f"The age {age} is Odd.")
            
    except ValueError as e:
        print(f"Invalid input error: {e}")

check_age()