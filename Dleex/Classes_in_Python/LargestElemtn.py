"""Large"""


def largest_element(element: list):
    elements = len(element[0])
    ele = element[0], len(element[0])
    for i in element:
        if len(i) > elements:
            elements = len(i)
            ele = i, len(i)
    return ele


name = ["Tayo", "Emmanuel", "Ope", "Oladele", "Abbbbbbbbbbfffffffff"]

print(largest_element(name))
