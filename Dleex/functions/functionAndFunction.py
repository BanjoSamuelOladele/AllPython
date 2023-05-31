"""idan"""


def double_function(func2: list, func1: list):
    elements = []
    func22 = set(func2)
    func111 = set(func1)
    return tuple(func22 & func111)
    # for i in func1:
    #     for n in func2:
    #         if i == n:
    #             elements.append(i)
    # return tuple(elements)


lst2 = [1, 4, 3]
lst1 = [1, 4, 5]

print(double_function(lst1, lst2))


def floating_number(flt1: float, flt2: float):
    if type(flt1) != float or type(flt2) != float:
        raise TypeError("float allowed")
    return float(flt1 + flt2)


# print(floating_number(2.2, 7))
def check_status(right):
    return True


def discount(price, discount):
    if price <= 0 or discount <= 0:
        raise ValueError("Zero value not allowed")
    if type(price) != float or type(discount) != float:
        raise ValueError("Integers allowed alone")
    if type(price) is str or type(discount) is str:
        raise TypeError("Integers allowed")
    return price - (price * (discount / 100))
