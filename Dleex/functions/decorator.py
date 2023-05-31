def decorate_func(func):
    def wrapper(*args, **kwargs):
        print("******************************************")
        print(func(*args, **kwargs))
        print("******************************************")

    return wrapper


@decorate_func
def name_func(name, age):
    return name_func


print(name_func("david", "35"))
