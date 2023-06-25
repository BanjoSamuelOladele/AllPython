from Bank import Bank
import unittest


class MyClassTest(unittest.TestCase):
    def test_bank_can_create_account(self):
        my_bank = Bank.Bank()
        my_bank.register_new_customer("firstName", "lastName", "1111")
        self.assertEquals(1, my_bank.size())
        my_bank.register_new_customer("firstName", "lastName", "password")
        my_bank.register_new_customer("firstName", "lastName", "password")
        self.assertEquals(3, my_bank.size())

    def test_bank_can_deposit_to_account(self):
        my_bank = Bank.Bank()
        my_bank.register_new_customer("firstName", "secondName", "2222")
        my_bank.deposit_to_account("22334455660", 3000)
        self.assertEquals(1, my_bank.size())
        print("----", my_bank.check_balance_via_account("22334455660", "2222"))
        self.assertEquals(3000, my_bank.check_balance_via_account("22334455660", "2222"))
