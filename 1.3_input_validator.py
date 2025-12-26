while True:
    age_input = input("Please enter your age here(18-99): ")

    #try catch stuff here
    try:
        age = int(age_input)
        if age < 18 or age > 99:
            raise ValueError("Age must be within set bounds of 18 and 99")
        else:
            print("Age accepted")
            break
                
    except ValueError:
        print("Invalid input. Please ener a number")