def list_to_zero(lst):
    if type(lst) is not list:
        raise TypeError("List expected")
    lst[0] = 0
    lst[len(lst) - 1] = 0
    return lst


lst = [1, 2, 3, 4, 5, 6, 7]
print(list_to_zero(lst))


def validate_name_mail(valid_name):
    if type(valid_name) is not str:
        raise TypeError("should contain letters")
    return f"{valid_name}@gmail.com"
