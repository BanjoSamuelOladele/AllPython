def card_number_length(card_number: str):
    return len(card_number)


def check_card_type(card_number: str):
    return check_card_number_for_type(card_number)


def check_card_number_for_type(card_number):
    if card_number.startswith("4"):
        return "Master Card"
    elif card_number.startswith("37"):
        return "America Express"
    elif card_number.startswith("5"):
        return "Visa"
    elif card_number.startswith("6"):
        return "Discover Card"
    else:
        return "Invalid Card"


def confirm_if_card_number_is_valid(card_number: str):
    list_of_card_number = []
    odd_number = 0
    even_number = 0
    total_number = 0
    insert_card_number_to_a_list(card_number, list_of_card_number)
    even_pos, odd_pos = character_on_odd_and_even_position(list_of_card_number)
    for number in odd_pos:
        odd_number = odd_number + int(number)
    for number in even_pos:
        even_number = even_number_product(even_number, number)
    total_number = odd_number + even_number
    return is_valid_response(total_number)


def is_valid_response(total_number):
    if total_number % 10 == 0:
        return "Valid Card Number"
    else:
        return "Invalid Card Number"


def character_on_odd_and_even_position(list_of_card_number):
    even_pos = list_of_card_number[len(list_of_card_number) - 2::-2]
    odd_pos = list_of_card_number[len(list_of_card_number) - 1::-2]
    return even_pos, odd_pos


def insert_card_number_to_a_list(card_number, list_of_card_number):
    for number in card_number:
        list_of_card_number.append(number)


def even_number_product(even_number, number):
    time = int(number) * 2
    if time > 9:
        even_number = product_greater_than9(even_number, time)
    else:
        even_number += time
    return even_number


def product_greater_than9(even_number, time):
    for n in range(2):
        remain = time % 10
        even_number += remain
        time //= 10
    return even_number


user_input = input("Enter your card number: ")
while len(user_input) >= 13 or len(user_input) <= 16:
    if len(user_input) < 13:
        print("card number is short")
        user_input = input("Enter your card number: ")
    if len(user_input) > 16:
        print("card number is long")
        user_input = input("Enter your card number: ")
else:
    print(confirm_if_card_number_is_valid("userinput"))
# if len(user_input) < 13:
#     print("card number too short")
#     user_input = input("Enter your card number: ")
# if len(user_input) > 16:
#     print("card number too long")
#     user_input = input("Enter your card number: ")
if user_input.isnumeric():
    print(confirm_if_card_number_is_valid("userinput"))
else:
    print("alphabet not allowed here")
    user_input = input("Enter your card number: ")
