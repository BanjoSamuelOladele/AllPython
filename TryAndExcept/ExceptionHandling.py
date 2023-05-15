"""Handling exceptions"""


def multiply(x, y):
    try:
        return x * y
    except TypeError:
        return f"Integers expected"


def invest(principal_amount, interest, ):
    try:
        for year in range(1, 4):
            annual_rate_of_return = principal_amount * interest
            new_principal = principal_amount + annual_rate_of_return
            principal_amount = new_principal
            print(f"year {year}:{principal_amount:,.2f}")
        return principal_amount
    except (NameError, SyntaxError):
        return f"dindirin"
    except ValueError:
        return f"wise Up!!"


print(invest(50000, 5))
