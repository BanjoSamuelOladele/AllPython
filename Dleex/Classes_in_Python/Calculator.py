"""Arithemtic calculation"""


def calculator(first_number, second_number, operator: str):
    match operator:
        case "+":
            return addition(first_number, second_number)
        case "-":
            return subtraction(first_number, second_number)
        case "*":
            return multiplication(first_number, second_number)
        case "/":
            return division(first_number, second_number)


def addition(first_number, second_number):
    return first_number + second_number


def subtraction(first_number, second_number):
    return first_number - second_number


def multiplication(first_number, second_number):
    return first_number * second_number


def division(first_number, second_number):
    return first_number / second_number


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("Enter the operation mode: ")

print(f"result is {calculator(first_number, second_number, operator)}")

