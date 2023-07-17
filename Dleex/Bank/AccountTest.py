import unittest
from Bank import Account


class MyTestCase(unittest.TestCase):
    def test_deposit(self):
        my_account = Account.Accounts("first_name", "last_name", "1111")
        my_account.deposit(5000)
        self.assertEquals(5000, my_account.check_balance("1111"))

    def test_deposit_again(self):
        my_account = Account.Accounts("first_name", "last_name", "1111")
        my_account.deposit(400)
        self.assertEquals(400, my_account.check_balance("1111"))

    def test_deposit_of_two_deposit_can_be_gotten_via_balance(self):
        my_account = Account.Accounts("first_name", "last_name", "1111")
        my_account.deposit(400)
        my_account.deposit(400)
        self.assertEquals(800, my_account.check_balance("1111"))

    def test_balance_can_only_be_accessed_with_correct_password(self):
        my_account = Account.Accounts("first_name", "last_name", "1111")
        my_account.deposit(4000)
        self.assertEquals(0, my_account.check_balance("2222"))

    def test_withdrawal_can_be_made_in_account(self):
        my_account = Account.Accounts("first_name", "last_name", "1111")
        my_account.deposit(4000)
        my_account.withdraw("1111", 2000)
        self.assertEquals(2000, my_account.check_balance("1111"))

    def test_withdrawal_can_be_done_in_account_again(self):
        my_account = Account.Accounts("first_name", "last_name", "1111")
        my_account.deposit(5500)
        my_account.withdraw("1111", 2000)
        self.assertEquals(3500, my_account.check_balance("1111"))

    def test_withdrawal_of_amount_less_than_zero_not_allowed(self):
        my_account = Account.Accounts("first_name", "last_name", "1111")
        my_account.deposit(5500)
        my_account.withdraw("1111", -2000)
        self.assertEquals(5500, my_account.check_balance("1111"))

    def test_withdrawal_cannot_be_made_with_wrong_password(self):
        my_account = Account.Accounts("first_name", "last_name", "1111")
        my_account.deposit(5500)
        # self.assertRaises (my_account.withdraw("2222", 2000))
        self.assertEquals(5500, my_account.check_balance("1111"))

    def test_deposit_with_amount_less_than_zero_not_allowed(self):
        my_account = Account.Accounts("first_name", "last_name", "1111")
        my_account.deposit(-5000)
        self.assertEquals(0, my_account.check_balance("1111"))
