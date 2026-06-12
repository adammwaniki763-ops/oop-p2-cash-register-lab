#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        item_total = price * quantity
        self.total += item_total

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
            "total_price": item_total,
        })

    def apply_discount(self):
        if self.discount == 0 or not self.previous_transactions:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        last_transaction = self.previous_transactions.pop()
        for _ in range(last_transaction["quantity"]):
            if self.items:
                self.items.pop()

        print(f"After the discount, the total comes to ${self.total:.0f}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["total_price"]

        for _ in range(last_transaction["quantity"]):
            if self.items:
                self.items.pop()
