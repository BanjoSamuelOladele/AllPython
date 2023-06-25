from Bank import Bank

bank = Bank.Bank()


def welcomeNote():
    print("""
    ======================
    Welcome to Wizard bank
    ======================
    """)


def bankingOption():
    welcomeNote()
    print("""
    1 -> Register Account
    2 -> Cash Transaction
    0 -> Exit
    """)
    user_input = input("enter your preferred choice: ")
    match user_input:
        case "1":
            registerNewCustomer()
        case "2":
            cash_transaction()


def cash_transaction():
    print("Welcome to the counter...")
    print("""
    1 -> Deposit
    2 -> Withdraw
    3 -> Transfer
    4 -> Check Balance
    9 -> Previous menu
    0 -> End Transaction
    """)


def cashing_option():
    user_input = input("Enter your preferred choice below: ")
    match user_input:
        case "1":
            depositAccount()
        case "4":
            checkBalance()


def registerNewCustomer():
    print("Enter the prompts below")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    password = input("Enter password: ")
    bank.register_new_customer(first_name, last_name, password)
    cash_transaction()


def depositAccount():
    print("Deposit To Account Window")
    account_number = input("Enter account number: ")
    amount = input("Enter amount: ")
    bank.deposit_to_account(account_number, amount)
    print("Transfer successful")
    cash_transaction()


def checkBalance():
    print("Check Account Balance Here")
    account_number = input("Enter account number: ")
    password = input("Enter password here: ")
    number = (bank.check_balance_via_account(account_number, password))
    print(number)
    cash_transaction()


print(bankingOption())
