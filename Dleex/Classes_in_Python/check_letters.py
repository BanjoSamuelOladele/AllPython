"""check letters"""


def check(name: str) -> list:
    lst = []
    for n in range(len(name)):
        if name[n].islower():
            lst.append(n)
    return lst


hello_str = "hello world"
print(hello_str[3:-2])



