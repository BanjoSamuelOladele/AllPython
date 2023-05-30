"""Using dictionary to create and check data"""


def cohort16_register(user_input: str):
    # user_input = input("Enter a name: ")
    register = {"esther": 23}
    if register.get(user_input.lower()):
        for value in register.values():
            return f"hi {user_input}, you are {value} years old"
    else:
        age = int(input("Enter age: "))
        register.update({user_input: age})
        for value in register.values():
            return f"hi {user_input}, you are {value} years old"


user_choice = input("Enter a name: ")
print(cohort16_register(user_choice))
