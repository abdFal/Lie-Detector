def person():
    print("What's your name?")
    name = input()
    print("Please enter your gender:")
    gender = input("1. Male\n2. Female\n3. Non-binary\n4. Prefer not to say\nYour choice (1/2/3/4): ")

    if gender == '1':
        confirmation = "Male."
    elif gender == '2':
        confirmation = "Female."
    elif gender == '3':
        confirmation = "Non-binary."
    elif gender == '4':
        confirmation = "You prefer not to say."
    else:
        confirmation = "Invalid choice."

    return name, confirmation

name, confirmation_message = person()
print("Name:", name)
print("Gender:", confirmation_message)
