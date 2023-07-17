def charOccurrences(inputs: str):
    first_letter = inputs[0]
    for i in inputs:
        if i == first_letter:
            inputs = inputs.replace(i, "$")
    return inputs


print(charOccurrences("nane"))


def multiOccurrences(inputs: str):
    for i in inputs:
        if i.count(inputs) > 1:
            inputs = inputs.replace(i, "$")
    return inputs


print(multiOccurrences("nane"))
