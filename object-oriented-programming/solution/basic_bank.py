from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Client:
    name: str
    pesel: int


@dataclass
class Account:
    number: int
    owner: Client
    amount: Decimal = 0.0


@dataclass
class Bank:
    accounts = []


@dataclass
class ATM:
    def input_card(self, card):
        pass

    def input_pin(self):
        pass

    def input_amount(self, amount):
        pass

    def give_money(self):
        pass

    def give_card(self):
        pass

    def _check_pin_number(self, pin):
        pass

    def _check_if_withdraw_possible(self):
        pass


jose = Client()
my_bank = Bank()
atm = ATM()


my_bank.open_account_for_client(jose)
my_bank.whats_my_account_number(jose)


atm.input_card(card)
atm.input_pin(pin)
atm.input_amount(amount)
atm.give_money()
atm.give_card()
